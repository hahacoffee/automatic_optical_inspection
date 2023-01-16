#???? cv2.add(img1,img2)
clc()
import cv2
import numpy as np
b=np.zeros([300,300,3],dtype='uint8')
g=np.zeros([300,300,3],dtype='uint8')
r=np.zeros([300,300,3],dtype='uint8')

b[100:200,50:250]=[200,0,0]
g[50:250,100:200]=[0,200,0]
r[75:225,75:225]=[0,0,200]
br=cv2.add(b,r)

cv2.imshow('br',br)
