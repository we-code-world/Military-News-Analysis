#!/usr/bin/env bash
export MODE="evaluate"
export BERT_DIR="/home/guest/bert/torch_roberta_wwm"
export ModelType="Weapon"
export ROOT="/home/guest/Rootpath"

export GPU_IDS="0,1"

# ep 8 bs 32
python Model.py \
--operation=$MODE \
--RootPath=$ROOT \
--BaseModelPath=$BERT_DIR \
--ModelType=$ModelType \
--GPU=$GPU_IDS \
--max_seq_len=320 \
--batch_size=16 \
--start_threshold=0.6 \
--end_threshold=0.6