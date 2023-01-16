
import numpy as np
import cv2
img=cv2.imread('D:\\University\\Automatic Optical Inspection\\HW\\HW0501.jpg')
a=np.empty((9,106,106,3))
k=0
for i in range(0,3):
    for j in range(0,3):
        x=106*i
        y=106*j
        a[k]=img[x:x+106,y:y+106]
        k=k+1
PIC=np.empty((318,318,3))
r=np.empty((9,106,106,3))
r[0]=a[7]
r[1]=a[6]
r[2]=a[4]
r[3]=a[0]
r[4]=a[3]
r[5]=a[1]
r[6]=a[8]
r[7]=a[2]
r[8]=a[5]
k=0
for i in range(0,3):
    for j in range(0,3):
        x=106*i
        y=106*j
        PIC[x:x+106,y:y+106]=r[k]
        k=k+1
cv2.imwrite('D:\\University\\Automatic Optical Inspection\\HW\\HW0501_output.jpg',PIC)
PIC1=cv2.imread('D:\\University\\Automatic Optical Inspection\\HW\\HW0501_output.jpg')
cv2.namedWindow('before',cv2.WINDOW_NORMAL)
cv2.namedWindow('after',cv2.WINDOW_NORMAL)
cv2.imshow('before',img)
cv2.imshow('after',PIC1)
cv2.waitKey(0)
cv2.destroyAllWindows()
