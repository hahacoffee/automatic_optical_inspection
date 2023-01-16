#????
clc()
import cv2
import numpy as np
img=cv2.imread('PIC.jpg',1)
rows,cols=img.shape[:2]
M=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)

dst=cv2.warpAffine(img,M,(2*rows,2*cols))
cv2.imshow('u',dst)