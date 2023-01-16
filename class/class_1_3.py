clc()
import cv2
import numpy as np
img=cv2.imread('D:\\Transfer\\Pictures\\2019-01\\PIC4.jpg')

#cx=100
#cy=100
#for i in range(cx-50,cx+50):
#    for j in range(cy-50,cy+50):
#        if (i-100)**2+(j-100)**2<50**2 and (i-100)**2+(j-100)**2>48**2:
#            img[i,j]=[255,255,255]

#x=np.linspace(50,100,100)
#y=np.sqrt(1-x**2)
#img[x,y]=[255,255,255]

cv2.circle(img,(100,100),50,(0,255,0),1)

cv2.imwrite('PIC4_1.jpg',img)

cv2.namedWindow('test',cv2.WINDOW_NORMAL)

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()