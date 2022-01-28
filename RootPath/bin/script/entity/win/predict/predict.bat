@set MODE="predict"
@set BaseModelPath="E:/Model/bert/torch_roberta_wwm"
@set ROOT="E:/Rootpath"

:: ep 8 bs 32
python Model.py ^
--operation=%MODE% ^
--RootPath=%ROOT% ^
--BaseModelPath=%BaseModelPath% ^
--max_seq_len=320 ^
--train_epochs=6 ^
--train_batch_size=14 ^
--learnRate=2e-5 ^
--otherLearnRate=2e-4 ^
--attack_train="pgd"