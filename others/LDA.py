#LDA two_classify
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_classification
'''
n,d = list(map(int,input().split()))

x = np.zeros((n,d))
y = np.zeros((n,1))

for i in range(n):
    c = np.array(list(map(int,input().split())))
    x[i] = c
print(x)
y = x[:,d-1]
print(y)
'''
x,y = make_classification(n_samples = 500,n_features=2,n_redundant = 0,n_classes = 2,n_informative = 1,n_clusters_per_class = 1,class_sep = 0.5,random_state = 10)

type1,type2 = np.unique(y)
x1 = np.array([x[i] for i in range(len(x)) if y[i] == type1])  #分类
x2 = np.array([x[i] for i in range(len(x)) if y[i] == type2])
u1 = np.mean(x1)  #均值
u2 = np.mean(x2)
c1 = x1 - u1 #[u1 for i in range(n)]
c2 = x2 - u2 #[u2 for i in range(n)]
Sw = np.cov(c1.T) + np.cov(c2.T)
print(Sw)
Sb = (u1-u2)*((u1-u2).T)
print(Sb)
V,A = np.linalg.eig(np.linalg.inv(Sw+np.identity(Sw.shape[0]))*Sb)
print(V,A)
plt.scatter(x1[:,0],x1[:,1])
plt.scatter(x2[:,0],x2[:,1])
xx = np.linspace(min(x[:,0]),max(x[:,1]),100)
yy = V[0]/V[1]*xx
plt.plot(xx,yy,color='green')
plt.show()