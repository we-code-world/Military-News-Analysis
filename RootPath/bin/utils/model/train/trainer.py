# coding=utf-8
"""
@author: Oscar
@license: (C) Copyright 2019-2022, ZJU.
@contact: 499616042@qq.com
@software: pycharm
@file: trainer.py
@time: 2020/9/2 15:19
"""
import copy
import torch
from torch.utils.data import DataLoader, RandomSampler
from classes.Utils.AuxiliaryModel import FGM, PGD
from utils.model.functionsUtils import load_model_on_gpu, swa, build_optimizer_and_scheduler, save_model


def train(opt, model, train_dataset, logger):
    swa_raw_model = copy.deepcopy(model)

    #  打乱顺序
    train_sampler = RandomSampler(train_dataset)

    #  构建训练集
    train_loader = DataLoader(dataset=train_dataset,
                              batch_size=opt.train_batch_size,
                              sampler=train_sampler,
                              num_workers=8)
    gpu_ids = opt.GPU
    #  将模型加载到GPU
    model, device = load_model_on_gpu(model, logger, gpu_ids)

    t_total = len(train_loader) * opt.train_epochs

    optimizer, scheduler = build_optimizer_and_scheduler(opt, model, t_total)

    # Train
    logger.info("***** Running training *****")
    logger.info(f"  Num Examples = {len(train_dataset)}")
    logger.info(f"  Num Epochs = {opt.train_epochs}")
    logger.info(f"  Total training batch size = {opt.train_batch_size}")
    logger.info(f"  Total optimization steps = {t_total}")

    global_step = 0

    model.zero_grad()

    fgm, pgd = None, None

    attack_train_mode = opt.attack_train.lower()
    if attack_train_mode == 'fgm':
        fgm = FGM(model=model)
    elif attack_train_mode == 'pgd':
        pgd = PGD(model=model)

    pgd_k = 3

    save_steps = t_total // opt.train_epochs
    eval_steps = save_steps

    logger.info(f'Save model in {save_steps} steps; Eval model in {eval_steps} steps')

    log_loss_steps = 20

    avg_loss = 0.

    #  训练

    for epoch in range(opt.train_epochs):

        for step, batch_data in enumerate(train_loader):
            print('Step: %d / %d ----> total loss: %.5f' % (global_step, t_total, avg_loss))

            model.train()

            for key in batch_data.keys():
                batch_data[key] = batch_data[key].to(device)

            loss = model(**batch_data)[0]

            loss.backward()

            if fgm is not None:
                fgm.attack()

                loss_adv = model(**batch_data)[0]

                loss_adv.backward()

                fgm.restore()
            elif pgd is not None:
                pgd.backup_grad()

                for _t in range(pgd_k):
                    pgd.attack(is_first_attack=(_t == 0))

                    if _t != pgd_k - 1:
                        model.zero_grad()
                    else:
                        pgd.restore_grad()

                    loss_adv = model(**batch_data)[0]

                    loss_adv.backward()

                pgd.restore()

            torch.nn.utils.clip_grad_norm_(model.parameters(), opt.max_grad_norm)

            optimizer.step()
            scheduler.step()
            model.zero_grad()

            global_step += 1

            if global_step % log_loss_steps == 0:
                avg_loss /= log_loss_steps
                logger.info('Step: %d / %d ----> total loss: %.5f' % (global_step, t_total, avg_loss))
                avg_loss = 0.
            else:
                avg_loss += loss.item()

            if global_step % save_steps == 0:
                save_model(model, global_step, logger)

    save_model(model, global_step, logger)
    swa(swa_raw_model, logger, swa_start=opt.swa_start)

    logger.info('Train done')
