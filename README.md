# Hierarchical-Multiple-Features-Combination-Model

# 文章链接
http://jxmu.xmu.edu.cn/upload/html/20200210.html
# 发表期刊
《厦门大学学报(自然科学版)》
# 摘要
针对维汉机器翻译中存在的维吾尔语形态复杂性和数据稀疏性问题, 提出了一种层次化融合多个维语语法特征的神经网络机器翻译模型。该模型采用四种特征（词干、词性、词缀、词缀形态）作为源端语言的附加信息，引入层次化多特征融合的神经网络结构，分层处理维语的词干级和词缀级特征，用于增强翻译系统对维语的句法结构和语义知识的学习能力，从而提高维汉机器翻译质量。
# Usage
OpenNMT-tf requires:
* Python >= 2.7
* TensorFlow >= 1.4 and < 2.0
# Command line
OpenNMT-tf comes with several command line utilities to prepare data, train, and evaluate models.
For all tasks involving a model execution, OpenNMT-tf uses a unique entrypoint: `onmt-main`.
* the **run** type: `train_and_eval`, `train`, `eval`, `infer`, `export`, or `score`
* the **model** type
* the **parameters** described in a YAML file
# Main Script
onmt-main <run_type> --model_type <model> --auto_config --config <config_file.yml>
