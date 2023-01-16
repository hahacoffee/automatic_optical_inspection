
import numpy as np
import matplotlib.pyplot as plt
alpha=eval(input("please give a angle:"))
anglephi=alpha
alpha=alpha*np.pi/180
anglephi=anglephi*np.pi/180
n0=1.5
a=1
k=(n0*a)/(n0-1)
l=k*(np.cos(alpha))
y=np.linspace(0,a,1000)
dy=(max(y)-min(y))/len(y)
Y=np.zeros(np.shape(y))
X=np.zeros(np.shape(y))
LY=len(y)
x=0
n=1.5
dx=dy/np.tan(anglephi)
for i in range(0,LY):
    dn=-((n0-1)/a)*dy
    dphi=dn/(n*np.tan(anglephi))
    dx=dy/np.tan(anglephi)
    if dx>0:
        n=n+dn
        x=x+dx
        anglephi=anglephi+dphi
        X[i]=x
    else:
        X[i]=x
        y[i]=y[i-1]
plt.plot(X,y)
plt.show()