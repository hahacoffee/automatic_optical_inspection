#???
clc()
import cv2
src=cv2.imread('shape.jpg')
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
bgray=cv2.medianBlur(gray,11)
ret,thresh=cv2.threshold(bgray,200,255,0)

image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img=cv2.drawContours(src,contours,-1,(0,255,0),3)
cv2.imshow('d',img)

for i in range(0,5):
    num=contours[i].shape[0]
    x=0
    y=0
    for j in range(0,num):
        x=x+contours[i][j][0,0]
        y=y+contours[i][j][0,1]
    x=x/num
    y=y/num
    x=round(x)
    y=round(y)
    print("x=",x,"y=",y)
    
