#!/usr/bin/env bash
export MODE="train"
export ModelType="Weapon"
export ROOT="/home/guest/Rootpath"
export BaseModelPath="/home/guest/bert/torch_roberta_wwm"

export GPU_IDS="0,1"

# ep 8 bs 32
python Model.py \
--operation=$MODE \
--RootPath=$ROOT \
--BaseModelPath=$BaseModelPath \
--ModelType=$ModelType \
--GPU=$GPU_IDS \
--train_epochs=6 \
--train_batch_size=16 \
--learnRate=2e-5 \
--otherLearnRate=2e-4 \
--attack_train="pgd"