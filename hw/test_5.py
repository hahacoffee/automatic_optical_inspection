clc()
import numpy as np
x=np.linspace(-10,10,20000) #mm
X=np.linspace(-.01,.01,300) # mm
z=60.0 #mm
f=60.01 #mm
l=0.6e-3 #mm
k=2*np.pi/l
i=0; dx=(max(x)-min(x))/len(x)
I=np.zeros(len(X))
for Xi in X:
    E=np.exp((-1j*k)*(-x**2/(2*f)+x**2/(2*z)-x*Xi/z+))*dx
    #Show=-x**2/2/f
    #print(Show)
    #print(x)
    #print(f)
    a=np.sum(E)
    I[i]=abs(a)**2
    i=i+1
I=dataObject(I)
X=dataObject(X)
fig=figure(1)
fig.plot1(I,X)