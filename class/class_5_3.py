clc()
import cv2
import numpy as np
img=cv2.imread("rectangle_circle1.jpg")
edges=cv2.Canny(img,150,200)
lines=cv2.HoughLines(edges,1,np.pi/180,100)
N=lines.shape[0] #numbers of the lines
for n in range(0,N-1):
    r=lines[n,0,0];q=lines[n,0,1]
    L=1000
    x0=int(r*np.cos(q));y0=int(r*np.sin(q))
    x1=int(x0+L*np.sin(q));y1=int(y0-L*np.cos(q))
    x2=int(x0-L*np.sin(q));y2=int(y0+L*np.cos(q))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
cv2.imshow('img',img)