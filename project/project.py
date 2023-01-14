# -*- coding: utf-8 -*-
"""
Created on Thu May 23 22:36:07 2019

@author: 訪客
"""
import os,dlib,glob,numpy
from skimage import io
import cv2
import imutils
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"C:\\Windows\\Fonts\\msjh.ttc", size=14)
predictor_path = "shape_predictor_68_face_landmarks.dat"
face_rec_model_path = "dlib_face_recognition_resnet_model_v1.dat"
faces_folder_path = "./資料庫圖片"

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

descriptors = []
candidate = []
filename = []

for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")): 
  filename.append(f)
  base = os.path.basename(f)                          
  candidate.append(os.path.splitext(base)[ 0])            
  img = io.imread(f)                                          

  dets = detector(img, 1)

  for k, d in enumerate(dets):               
    shape = sp(img, d)

    face_descriptor = facerec.compute_face_descriptor(img, shape,100,0.25)

    v = numpy.array(face_descriptor)
    descriptors.append(v)
    
pointer=0

cap = cv2.VideoCapture(0)

cap.set(cv2. CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2. CAP_PROP_FRAME_HEIGHT, 720)

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor( 'shape_predictor_68_face_landmarks.dat')

while(cap.isOpened()):

  ret, frame = cap.read()                              

  face_rects, scores, idx = detector.run(frame, 0)           
                                                            
  for i, d in enumerate(face_rects):
    
    if scores[i] > 0.6 :
       pointer=1

    landmarks_frame = cv2.cvtColor(frame, cv2. COLOR_BGR2RGB)

    shape = predictor(landmarks_frame, d)
 
  cv2.imshow( "Face Detection", frame)

  if cv2.waitKey(10) == 27:
     break
  if pointer == 1:
    break
cv2.imwrite("get_image.jpg",frame)

cap.release()

cv2.destroyAllWindows()

img_path = "D:\\University\\Automatic_Optical_Inspection\\Project\\get_image.jpg" 

img = io.imread(img_path)
dets = detector(img, 1)

dist = [] 
for k, d in enumerate(dets):
  shape = sp(img, d)
  face_descriptor = facerec.compute_face_descriptor(img, shape,100,0.25)
  d_test = numpy.array(face_descriptor)

  x1 = d.left()
  y1 = d.top()
  x2 = d.right()
  y2 = d.bottom()
  
  cv2.rectangle(img, (x1, y1), (x2, y2), ( 0, 255, 0), 4, cv2. LINE_AA)

  for i in descriptors:
    dist_ = numpy.linalg.norm(i-d_test)                                                                                          # ，(i-d_test)矩陣餒每個元素平方後相加開根號
    dist.append(dist_)
    
c_d = dict( zip(candidate,dist))
c_d_1 = dict( zip(filename,dist))

cd_sorted = sorted(c_d.items(), key = lambda d:d[ 1])
cd_sorted_1 = sorted(c_d_1.items(), key = lambda d:d[ 1])

rec_name = cd_sorted[ 0][ 0]
rec_dist = cd_sorted[ 0][ 1]

rec_name_1 = cd_sorted[ 1][ 0]
rec_dist_1 = cd_sorted[ 1][ 1]

rec_name_2 = cd_sorted[ 2][ 0]
rec_dist_2 = cd_sorted[ 2][ 1]

rec_dist = round((100-((round(rec_dist,4)-0.3)*(10/7)*100)),2)
if(rec_dist>=100):
    rec_dist=99.98
    
rec_dist_1 = round((100-((round(rec_dist_1,4)-0.3)*(10/7)*100)),2)
if(rec_dist_1>=100):
    rec_dist_1=99.98
    
rec_dist_2 = round((100-((round(rec_dist_2,4)-0.3)*(10/7)*100)),2)
if(rec_dist_2>=100):
    rec_dist_2=99.98
      
rec_dist = str(rec_dist)
rec_dist_1 = str(rec_dist_1)
rec_dist_2 = str(rec_dist_2)

rec_name_show_1 = cd_sorted_1[ 0][ 0]
rec_name_show_2 = cd_sorted_1[ 1][ 0]
rec_name_show_3 = cd_sorted_1[ 2][ 0]

img2 = io.imread(rec_name_show_1)
img3 = io.imread(rec_name_show_2)
img4 = io.imread(rec_name_show_3)

dets = detector(img2, 1)
for k, d in enumerate(dets):
  shape = sp(img2, d)
  face_descriptor = facerec.compute_face_descriptor(img2, shape,100,0.25)

  x1_1 = d.left()
  y1_1 = d.top()
  x2_1 = d.right()
  y2_1 = d.bottom()
  
  cv2.rectangle(img2, (x1_1, y1_1), (x2_1, y2_1), ( 0, 255, 0), 4, cv2. LINE_AA)
  
dets = detector(img3, 1)
for k, d in enumerate(dets):
  shape = sp(img3, d)
  face_descriptor = facerec.compute_face_descriptor(img3, shape,100,0.25)

  x1_2 = d.left()
  y1_2 = d.top()
  x2_2 = d.right()
  y2_2 = d.bottom()

  cv2.rectangle(img3, (x1_2, y1_2), (x2_2, y2_2), ( 0, 255, 0), 4, cv2. LINE_AA)
  
dets = detector(img4, 1)
for k, d in enumerate(dets):
  shape = sp(img4, d)
  face_descriptor = facerec.compute_face_descriptor(img4, shape,100,0.25)

  x1_3 = d.left()
  y1_3 = d.top()
  x2_3 = d.right()
  y2_3 = d.bottom()
  
  cv2.rectangle(img4, (x1_3, y1_3), (x2_3, y2_3), ( 0, 255, 0), 4, cv2. LINE_AA)

img = imutils.resize(img,height = 720, width = 1280)
img2 = imutils.resize(img2,height =720, width = 1280 )
img3 = imutils.resize(img3,height =720, width = 1280 )
img4 = imutils.resize(img4,height =720, width = 1280 )

plt.figure(1)
plt.subplot(2,3,2)
plt.title("長得像誰 ?", fontproperties=font)
plt.imshow(img)

plt.subplot(2,3,4)
plt.title("最像的人 : "+rec_name, fontproperties=font)
plt.imshow(img2)
plt.legend(loc='upper right',title=rec_dist+'%')

plt.subplot(2,3,5)
plt.title("第二像的人 : "+rec_name_1, fontproperties=font)
plt.imshow(img3)
plt.legend(loc='upper right',title=rec_dist_1+'%')

plt.subplot(2,3,6)
plt.title("第三像的人 : "+rec_name_2, fontproperties=font)
plt.imshow(img4)
plt.legend(loc='upper right',title=rec_dist_2+'%')

plt.show()

cv2.waitKey( 0)
cv2.destroyAllWindows()