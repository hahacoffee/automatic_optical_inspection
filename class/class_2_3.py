clc()
import cv2
import time
img=cv2.imread('PIC.jpg',1)
tStart=time.time() #????
b,g,r=cv2.split(img)
tEnd=time.time() #????
tcost=(tEnd-tStart)*1000
print(tcost)
cv2.imshow('bgr',img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
cv2.waitKey()
cv2.destroyAllWindow()