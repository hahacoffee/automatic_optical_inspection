import numpy as np
x=np.linspace(-1,1,100)
q=np.linspace(-1,1,200)*np.pi/180
l=0.6e-2
k=2*np.pi/l
i=0
I=np.zeros(len(q))
for qi in q:
    a=np.sum(np.exp(-1j*k*x*qi))
    I[i]=abs(a)**2
    i=i+1
I=dataObject(I)
q=dataObject(q)
plot1(I,q*180/np.pi)
