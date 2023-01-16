clc()
import numpy as np
import cv2
src=cv2.imread('euro.jpg')
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
bgray=cv2.medianBlur(gray,33)
ret,thresh=cv2.threshold(bgray,200,255,0)

image,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img=cv2.drawContours(src,contours,-1,(0,255,0),3)
cv2.imshow('d',img)
