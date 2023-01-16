clc()
import cv2
import numpy as np
fig=figure(1,rows=1,cols=2)
x=np.linspace(0,1000,1000)
X,Y=np.meshgrid(x,x)
Z=np.zeros(X.shape)
Z[200:300,200:300]=10
Z[500:700,500:700]=200
Z=dataObject(Z);Zl=dataObject()
filter("lowPassFilter",Z,Zl,99,99)
filter("saveJPG",Zl,'testimg.jpg','gray')
img=cv2.imread('testimg.jpg',0)
rat,thresh=cv2.threshold(img,120,255,0)
edges=cv2.Canny(thresh,180,200)
fig.plot(img,areaIndex=0)
fig.plot(edges,areaIndex=1)