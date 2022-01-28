@set MODE="train"
@set BERT_DIR="E:\\Model\\bert\\torch_roberta_wwm"
@set ModelType="Attribution"
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
--train_epochs=6 ^
--train_batch_size=16 ^
--learnRate=2e-5 ^
--otherLearnRate=2e-4 ^
--attack_train="pgd"