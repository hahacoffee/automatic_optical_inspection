import cv2
import numpy as np
b=np.zeros([300,300,3],dtype='uint8')
r=np.zeros([300,300,3],dtype='uint8')
b[100:200,50:250]=[200,0,0]
r[75:225,75:225]=[0,0,200]
br=cv2.addWeighted(b,0.7,r,0.3,0)
cv2.imshow('br',br)