#!/usr/bin/env bash
export BERT_TYPE="roberta_wwm"  # roberta_wwm / ernie_1  / uer_large
export MODE="train"
export ModelType="Trigger"
export ROOT="/home/guest/Rootpath"
export BaseModelPath="/home/guest/bert/torch_roberta_wwm"
export GPU_IDS="0"
# ep 8 bs 32
python3 Model.py \
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

export ModelType="TimeLoc"
python3 Model.py \
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

export ModelType="Weapon"
python3 Model.py \
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

export ModelType="Country"
python3 Model.py \
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

export ModelType="SubObj"
python3 Model.py \
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
