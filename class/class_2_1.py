clc()
import numpy as np
import cv2
img=cv2.imread('PIC.jpg',1)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img',img)
cv2.imshow('imgGray',imgGray)
cv2.watKey(0)
cv2.destroyAllwindows()