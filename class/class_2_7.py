#???? cv2.resize()
import cv2
import numpy as np
img=cv2.imread('PIC.jpg')
res2=cv2.resize(img,(100,100))
res=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
cv2.imshow('o',img)
cv2.imshow('r',res)