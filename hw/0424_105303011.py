clc()
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5,5,100)
h=np.cos(x)
d=5
dis1=d-h
X1,Y1=np.meshgrid(dis1,dis1)
k=2*np.pi/10

E11=np.exp(1j*k*0)
E21=np.exp(1j*k*(X1)*2)
I1=abs(E11+E21)**2

dis2=d-h+(10/8)
X2,Y2=np.meshgrid(dis2,dis2)
E12=np.exp(1j*k*0)
E22=np.exp(1j*k*(X2)*2)
I2=abs(E12+E22)**2

dis3=d-h+2*(10/8)
X3,Y3=np.meshgrid(dis3,dis3)
E13=np.exp(1j*k*0)
E23=np.exp(1j*k*(X3)*2)
I3=abs(E13+E23)**2

dis4=d-h+3*(10/8)
X4,Y4=np.meshgrid(dis4,dis4)
E14=np.exp(1j*k*0)
E24=np.exp(1j*k*(X4)*2)
I4=abs(E14+E24)**2

plt.figure(1)

plt.subplot(2,2,1)
plt.title("move 0")
plt.imshow(I1,cmap='gray')
plt.subplot(2,2,2)
plt.title("move pi/2")
plt.imshow(I2,cmap='gray')
plt.subplot(2,2,3)
plt.title("move pi")
plt.imshow(I3,cmap='gray')
plt.subplot(2,2,4)
plt.title("move 3pi/4")
plt.imshow(I4,cmap='gray')

DX,DY=np.meshgrid(d,d)
PHI=np.arctan((I2-I4)/(I1-I3))
H2=(PHI*(10/(4*np.pi)))

HX1,HY1=np.meshgrid(h,h)

plt.figure(2)
plt.subplot(1,2,1)
plt.title("set function")
plt.imshow(HX1,cmap='gray')
plt.subplot(1,2,2)
plt.title("function by\n Spatial Phase-Shifting Interferometry")
plt.imshow(H2,cmap='gray')

