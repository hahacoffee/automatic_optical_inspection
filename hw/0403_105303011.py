clc()
import numpy as np
DIS=np.linspace(0,100,1000)
a=10+DIS*0.1
b=20+DIS*(-0.1)
arc=(90*np.pi/180)/1000
deang=np.linspace(-45,45,1000)
ang=deang*np.pi/180
i=0
D=np.zeros((1000,1000))
for ang1 in ang:
    end=(np.sqrt((a*np.cos(ang1))**2+(b*np.sin(ang1))**2))**2*arc/2
    D[i]=end
    i=i+1
deang=np.linspace(45,135,1000)
ang=deang*np.pi/180
i=0
A=np.zeros((1000,1000))
for ang1 in ang:
    end=(np.sqrt((a*np.cos(ang1))**2+(b*np.sin(ang1))**2))**2*arc/2
    A[i]=end
    i=i+1
deang=np.linspace(135,225,1000)
ang=deang*np.pi/180
i=0
B=np.zeros((1000,1000))
for ang1 in ang:
    end=(np.sqrt((a*np.cos(ang1))**2+(b*np.sin(ang1))**2))**2*arc/2
    B[i]=end
    i=i+1
deang=np.linspace(225,315,1000)
ang=deang*np.pi/180
i=0
C=np.zeros((1000,1000))
for ang1 in ang:
    end=(np.sqrt((a*np.cos(ang1))**2+(b*np.sin(ang1))**2))**2*arc/2
    C[i]=end
    i=i+1
A1=np.sum(A,axis=0)
B1=np.sum(B,axis=0)
C1=np.sum(C,axis=0)
D1=np.sum(D,axis=0)
FES=(A1+C1)-(B1+D1)
DIS=dataObject(DIS)
FES=dataObject(FES)
plot1(FES,DIS)