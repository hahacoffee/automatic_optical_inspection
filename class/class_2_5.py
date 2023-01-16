#????
clc()
import cv2
import numpy as np
img=cv2.imread('PIC.jpg',1)
b,g,r=cv2.split(img)
zeros=np.zeros(img.shape[:2],dtype="uint8")
blue=cv2.merge([b,zeros,zeros])
green=cv2.merge([zeros,g,zeros])
red=cv2.merge([zeros,zeros,r])
cv2.imshow('b',blue)
cv2.imshow('g',green)
cv2.imshow('r',red)