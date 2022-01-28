### 项目目录说明

```shell
bin                                     # 所有python代码的根目录
├── classes                             # 所有类相关代码
│   ├── Dataset
│   │   └── Bert                        # dataset数据集类
│   ├── Example
│   │   └── Bert                        # 读入数据构建的example类
│   ├── Feature
│   │   └── Bert                        # 编码feature类
│   ├── Model
│   │   └── Bert                        # 模型类
│   ├── Utils
│   │   └── AuxiliaryModel.py           # 所有python代码的根目录
|
├──—log                                 # 所有python代码的根目录
│   ├── model.txt                       # 所有python代码的根目录
│   └── model_new.txt                   # 数据文件夹
│
├──—model                               # 数据文件夹
│   ├── model_evaluate.py               # 模型输出结果      
│   ├── model_train.py                  # 模型输出结果 
│   └── model_predict.py                # 数据文件夹
│
├──—script                              # 数据文件夹
│   ├── entity                          # 实体模型的运行脚本存放文件夹      
│   │   ├── linux                       # linux版本 
│   │   └── win                         # windows版本 
│
├──—utils                               # 数据文件夹
│   ├── dataset                         # 数据文件夹                    
│   │   ├── buildDataset.py             # 构建pipeline需要的数据集
│   │   └── getDataset.py               # 构建模型训练和评估的数据集
│   ├── file                            # 文件处理
│   │   ├── path.py                     # 路径处理相关函数
│   │   └── read.py                     # 文件处理相关函数
│   ├── model                           # 模型相关辅助程序存储地址
│   │   ├── evaluate
│   │   │   └── evaluator.py            # 评估相关
│   │   ├── predict
│   │   │   └── predicter.py            # 预测相关
│   │   ├── train
│   │   │   └── trainer.py              # 训练相关
│   │   ├── buildModel.py               # 根据模型类型选择不同类构建一个新的模型
│   │   ├── functionsUtils.py           # 模型处理过程中的相关辅助处理函数
│   │   └── getModel.py                 # 根据模型类型选择不同类读取已保存的模型参数
│   ├── lock.py                         # 锁文件 
│   ├── logger.py                       # 日志文件设置 
│   └── options.py                      # 输入参数的设置
│
└── Model.py                            # 模型相关主代码，通过option控制执行内容
```

