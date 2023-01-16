#????
clc()
import cv2
import numpy as np
img=cv2.imread('PIC.jpg',0)
rows,cols=img.shape[:2]
M=np.float32([[1,0,100],[0,1,50]])
dst=cv2.warpAffine(img,M,(rows,cols))
cv2.imshow('u',dst)