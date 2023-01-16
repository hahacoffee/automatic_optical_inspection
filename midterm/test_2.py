clc()
import numpy as np
f=100
fx=100
fy=120
for delta in range(-20,20)
fd=np.array(f-delta)
P=np.array([[[1],[0]],[]])
L0=np.array([[1,0],[(-1/f),1]])
F=np.array([[[1,fd],[0,1]],[]])
L1=np.array([[[1,0],[(-1/fx),1]],[]])
L2=np.array([[[1,0],[(-1/fy),1]],[]])
L=np.array([[[1,300],[0,1]],[]])
T=np.array([[[1,109.0909],[0,1]],[]])
AA=T*L1*L*L0*F*F*L0*P
BB=T*L2*L*L0*F*F*L0*P

a=AA[0][0][:]
b=BB[0][0][:]

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
delta=dataObject(delta)
FES=dataObject(FES)
plot1(FES,delta)