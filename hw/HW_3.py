clc()
import numpy as np
import matplotlib.pyplot as plt
alpha1=eval(input("please give a angle:"))
alpha1=alpha1*np.pi/180
n0=1.5
a=1
dy=0.001
y=0
Y=np.zeros(1000)
X=np.zeros(1000)
x=0
X[0]=x
Y[0]=y
for i in range(1,999):
    y=y+dy
    n=n0-(((n0-1)/a)*y)
    alpha2=np.arcsin((n0/n)*np.sin(alpha1))
    s=dy*np.tan(alpha1)
    print(s)
    x=x+s
    X[i]=x
    Y[i]=y
    n0=n
    alpha1=alpha2
plt.plot(X,Y)
plt.show()