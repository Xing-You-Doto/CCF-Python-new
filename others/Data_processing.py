#计数器,分类计数
from collections import Counter
obj = Counter('aabbccc')
#obj = Counter({'a':2,'b':2,'c':3})
#obj.items() = dict_items([('a',2),('b',2),('c',3)])
#sorted(a.items()) = [('a', 2), ('b', 2), ('c', 3)]


import pandas as pd
#缺失值处理
df.fillna(num,inplace=True) #inplace源数据做相应替换
df.fillna(df.mean())
df.fillna(method='pad') #用后一个值做填充
df.fillna(method="bfill") #用前一个值做填充
df.interpolate()#用前一个和后一个值平均做填充
df.dropna()#删除缺失值,默认为行，axis=1 列删除

df = df.drop_duplicates()#删除重复行
df = df.drop(column_name,axis = 1)#删除字段，特征

#特征缩放,处理不同特征数值范围不同的问题
#(x-mean)/(max-min),(x-min)/(max-min),(标准化)(x-mean)/α
from sklearn.preprocessing import MinMaxSaler
clf = MinMaxSaler(feature_range=(min,max))#feature_range选择归一化后的取值范围
data = clf.fit_transform(data)

from sklearn.preprocessing import StandardScaler
#相同操作

#第二种
df = (df-np.mean())/(np.max(df)-np.min(df))

#样本不平衡
#第一种方法   上采样，过采样
from imlearn.over_sampling import RandomOverSample
ros = RandomOverSample(random_state = 0)
X_resamples, y_resampled = ros.fit_sample(X,y)
#第二种方法   通过一定规则生成新的变量
from imblearn.over_sampling import SMOTE,ADASYN
X_resamples,y_resampled = SMOTE(kind = 'borderlinel').fit_sample(X,y)
#第三种方法  下采样，欠采样
from imlearn.under_sampling import RandomUnderSample

#集成方法,样本抽取
from imblearn.dataset import make_imbalance
ratio = {0:20,1:20,2:30}#第一类抽20，二类20
X_resamples,y_resampled = make_imbalance(X,y,ratio=ratio)

#识别异常值
#一、简单的统计分析
#二、3α原则  正太分析 概率极小事件
#三、箱型图分析
#四、调用聚类算法，DBSCAN
#箱型图
import seaborn as sns
import matplotlib.pyplot as plt

#********************特征工程***************
#连续变量离散化  分箱/自适应binning
#类别特征-编码   LabelEncoder one-hot编码(用于样本之间距离的计算或相似度的计算，将离散特征扩展到欧氏空间)
from sklearn import preprocessing
enc = preprocessing.OneHotEncoder(categories='auto')
#时间特征
from pandas import to_datatime
import time #自定义转换
#特征构建
#一、用基因编程创建新特征
#二、根据业务分析创建特征
#特征选择
#过滤式Flitering 根据特征重要程度进行排序，方差越大，与相关变量相关系数越高
#包裹是Wrapper 前向选择  后向选择
#嵌入式embedding GBDT Xgboost