clc()
import cv2
import numpy as np
src=cv2.imread('paper.png')
gray=cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
gray=cv2.medianBlur(gray,7)
edges=cv2.Canny(gray,50,100)
circles=cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,60,param1=100,param2=20,minRadius=10,maxRadius=20)
circles=np.int16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(src,(i[0],i[1]),i[2],(0,0,255),2)
    cv2.circle(src,(i[0],i[1]),2,(0,255,0),3)
cv2.imshow('gray',gray)
cv2.imshow('edges',edges)

cv2.imshow('src',src)
circles.shape[1]

print("we have",circles.shape[1],"numbers of o")