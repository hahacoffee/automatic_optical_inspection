clc()
import cv2
img=cv2.imread('D:\\Transfer\\Pictures\\2019-01\\PIC4.jpg')

img[0:100,0:100]=[255,255,255]
img.item(100,100,2)
img.itemset((100,100,2),255)
cv2.imshow('test',img)

cv2.waitKey(0)
cv2.destroyAllWindows()