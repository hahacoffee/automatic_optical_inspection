clc()
import numpy as np
import matplotlib.pyplot as plt
alpha=eval(input("please give a angle:"))
n0=1.5
a=1
k=(n0*a)/(n0-1)
l=k*(np.cos((alpha*180)/(np.pi)))
y=0
dx=0.01
x=np.linspace(0,2,1000)
dx=(max(x)-min(x))/len(x)
Y=np.zeros(np.shape(x))
for i in range(0,len(x)):
    y=y+(((((k-y)**2)-(l**2))/(l**2))**0.5)*dx
    Y[i]=y
plt.plot(x,Y)
plt.show()