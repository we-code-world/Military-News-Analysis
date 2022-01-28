@set MODE="evaluate"
@set BERT_DIR="E:\\Model\\bert\\torch_roberta_wwm"
@set ModelType="TimeLoc"
@set ROOT="E:/Rootpath"

@set GPU_IDS="0"

:: ep 8 bs 32
python Model.py ^
--operation=%MODE% ^
--RootPath=%ROOT% ^
--BaseModelPath=%BERT_DIR% ^
--ModelType=%ModelType% ^
--GPU=%GPU_IDS% ^
--max_seq_len=320 ^
--batch_size=16 ^
--start_threshold=0.6 ^
--end_threshold=0.6