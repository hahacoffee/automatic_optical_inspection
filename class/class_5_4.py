clc()
import cv2
import numpy as np
img=cv2.imread('2rectangle.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
edges=cv2.Canny(gray,50,150)
lines=cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength=10,maxLineGap=20)
N=lines.shape[0]
for n in range(N):
    x1=lines[n,:,0]
    y1=lines[n,:,1]
    x2=lines[n,:,2]
    y2=lines[n,:,3]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)
cv2.imshow('img',img)