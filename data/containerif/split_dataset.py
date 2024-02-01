# --------------------------------------------------
# 文件名: split_dataset
# 创建时间: 2024/2/1 10:17
# 描述: 把原始数据集划分成3分
# 作者: WangYuanbo
# --------------------------------------------------
# 读取csv数据集
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('dataset.csv')  # 把你的csv文件路径替换成'yourfile.csv'

# 切分训练集和测试集（比例为8:2）
train, test = train_test_split(data, test_size=0.2, random_state=42)

# 在训练集中再切分出验证集（比例是原始训练集的20%，也就是最初的80%的20%即16%，从而确保训练集:验证集:测试集 = 64%:16%:20%）
train, valid = train_test_split(train, test_size=0.2, random_state=42)
train.to_csv('train.csv')
valid.to_csv('valid.csv')
test.to_csv('test.csv')
