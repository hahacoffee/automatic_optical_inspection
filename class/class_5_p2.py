#???
clc()
import cv2
import numpy as np
img=cv2.imread('IMG_3973.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
edges=cv2.Canny(gray,60,80)
lines=cv2.HoughLinesP(edges,1,np.pi/180,20,minLineLength=50,maxLineGap=200)
N=lines.shape[0]
for n in range(N):
    x1=lines[n,:,0]
    y1=lines[n,:,1]
    x2=lines[n,:,2]
    y2=lines[n,:,3]
    xp1=lines[n-1,:,0]
    yp1=lines[n-1,:,1]
    xp2=lines[n-1,:,2]
    yp2=lines[n-1,:,3]
    
    dx=x2-x1
    dy=y2-y1
    m=dy/dx
    dxp=xp2-xp1
    dyp=yp2-yp1
    mp=dyp/dxp
    
    a1=x2-x1
    a2=y2-y1
    b1=xp2-xp1
    b2=yp2-yp1
    up=a1*b1+a2*b2
    dow=np.sqrt(a1**2+a2**2)*np.sqrt(b1**2+b2**2)
    
    dif=np.abs(m-mp)
    if dif>2:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)
        cv2.line(img,(xp1,yp1),(xp2,yp2),(0,0,255),3)
        theta=np.arccos(up/dow)
        theta=theta*360/2*np.pi
        while theta>180:
            theta=theta-360
        if theta<0:
            theta=-theta
        print(theta)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.imshow('img',img)
#cv2.namedWindow('edges',cv2.WINDOW_NORMAL)
#cv2.imshow('edges',edges)