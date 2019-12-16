#LDA muti_classify
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
x = iris['data'][:,1:3]
y = iris['target']
n = x.shape[0]
type_ = np.unique(y)
listx = []   #数据按类别分类
avgx = []   #均值
swx = []    #类内散度矩阵
for j in range(len(type_)):
	listx.append(np.array([x[i] for i in range(n) if y[i] == type_[j]]))
	avgx.append(np.mean(listx[j]))
	swx.append(np.dot((listx[j] - avgx[j]).T,(listx[j] - avgx[j])))
uu = np.mean(x)  #全局均值
St = np.dot((x - uu).T,(x - uu))	
Sw = sum(swx)
Sb = St - Sw
print(Sb)
print(Sw)
V,A = np.linalg.eig(np.linalg.inv(Sw+np.identity(Sw.shape[0]))*Sb)



for i in range(len(listx)):
	plt.scatter(listx[i][:,0],listx[i][:,1])
xx = np.linspace(min(x[:,0]),max(x[:,0]),100)
print(V,A)
yy = A[0][0]/A[1][0]*xx
plt.plot(xx,yy,color='green')
plt.show()