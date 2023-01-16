clc()
import numpy as np
import cv2
import matplotlib.pyplot as plt
x=np.linspace(-3,3,300)
X,Y=np.meshgrid(x,x)
h=np.exp(-(X**2)-(Y**2))
s=np.random.random([300,300])*10
k=2*np.pi/0.6
l2=1000
l1=1000
I1=2+2*np.cos(2*k*(l2-l1+s))
I2=2+2*np.cos(2*k*(l2-l1+s+h))
I3=cv2.add(I1,I2)
cv2.imwrite('HW0508_output_I1.jpg',I1)
cv2.imwrite('HW0508_output_I2.jpg',I2)
cv2.imwrite('HW0508_output_I1+I2.jpg',I3)
plt.figure(1)
plt.title("I1")
plt.imshow(I1,cmap='gray')
plt.figure(2)
plt.title("I2")
plt.imshow(I2,cmap='gray')
plt.figure(3)
plt.title("I1+I2")
plt.imshow(I3,cmap='gray')
plt.show()