#???
clc()
import cv2
import numpy as np
src=cv2.imread('paper.png')
gray=cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
gray=cv2.medianBlur(gray,9)
edges=cv2.Canny(gray,50,100)
circles=cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,60,param1=100,param2=20,minRadius=10,maxRadius=20)
circles=np.int16(np.around(circles))
print("we have",circles.shape[1],"numbers of o")