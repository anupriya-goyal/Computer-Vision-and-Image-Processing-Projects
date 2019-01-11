
# coding: utf-8

# In[2]:


UBIT =  'anupriya'; 
import numpy as np; 
np.random.seed(sum([ord(c) for c in UBIT]))
#task2 code for all parts

import cv2
import random
#References for task2 are as follows:
#1.https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_calib3d/py_depthmap/py_depthmap.html
#2.https://docs.opencv.org/3.4.3/da/de9/tutorial_py_epipolar_geometry.html
#3.https://docs.opencv.org/3.4/da/df5/tutorial_py_sift_intro.html
#4.https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html

image1= cv2.imread("tsucuba_left.png",0)
image2= cv2.imread("tsucuba_right.png",0)
sift =cv2.xfeatures2d.SIFT_create()

keypoint1,d1 = sift.detectAndCompute(image1,None)
keypoint2,d2 = sift.detectAndCompute(image2,None)

image1_keypoint = cv2.drawKeypoints(image1,keypoint1,None)
image2_keypoint = cv2.drawKeypoints(image2,keypoint2,None)


# BFMatcher with default params
burteforce_matcher= cv2.BFMatcher()
total_matches  = burteforce_matcher.knnMatch(d1,d2, k=2)

# Apply ratio test
good_points = []
for m,n in total_matches:
    if m.distance < 0.75*n.distance:
        good_points.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
image_knn = cv2.drawMatchesKnn(image1,keypoint1,image2,keypoint2,good_points,None,flags=2)

cv2.imwrite("task2_sift1.png", image1_keypoint)
cv2.imwrite("task2_sift2.png", image2_keypoint)
cv2.imwrite("task2_matches_knn.jpg",image_knn)

#task2 part3 selecting inlier matche pairs and computing epiline 
# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params,search_params)
total_matches = flann.knnMatch(d1,d2,k=2)

points_good = []
pts1 = []
pts2 = []

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(total_matches):
    if m.distance < 0.75*n.distance:
        points_good.append(m)
        pts2.append(keypoint2[m.trainIdx].pt)
        pts1.append(keypoint1[m.queryIdx].pt)
pts1 = random.sample(pts1, 10)
pts2 = random.sample(pts2, 10)


pts1 = np.int32(pts1)
pts2 = np.int32(pts2)
#print(pts1)
#print(pts2)
F, mask = cv2.findFundamentalMat(pts1,pts2,cv2.FM_LMEDS)
print("The fundamental matrix is:")
print(F)
pts1 = pts1[mask.ravel()==1]
pts2 = pts2[mask.ravel()==1]
              # a sequence or set will work here.
                           # set the number to select here.

def drawlines(image1,image2,lines,pts1,pts2):
    ''' img1 - image on which we draw the epilines for the points in img2
        lines - corresponding epilines '''
    r,c = image1.shape
    image1 = cv2.cvtColor(image1,cv2.COLOR_GRAY2BGR)
    image2 = cv2.cvtColor(image2,cv2.COLOR_GRAY2BGR)
    
    for r,pt1,pt2 in zip(lines,pts1,pts2):
        color = tuple(np.random.randint(0,255,3).tolist())
        x0,y0 = map(int, [0, -r[2]/r[1] ])
        x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
        image1 = cv2.line(image1, (x0,y0), (x1,y1), color,1)
        image1 = cv2.circle(image1,tuple(pt1),5,color,-1)
        image2 = cv2.circle(image2,tuple(pt2),5,color,-1)
    return image1,image2
    
# Find epilines corresponding to points in right image (second image) and
# drawing its lines on left image
lines1 = cv2.computeCorrespondEpilines(pts2.reshape(-1,1,2), 2,F)
lines1 = lines1.reshape(-1,3)
image5,image6 = drawlines(image1,image2,lines1,pts1,pts2)

# Find epilines corresponding to points in left image (first image) and
# drawing its lines on right image
lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1,1,2), 1,F)
lines2 = lines2.reshape(-1,3)
image3,image4 = drawlines(image2,image1,lines2,pts2,pts1)
cv2.imwrite("task2_epi_left.jpg",image5)
cv2.imwrite("task2_epi_right.jpg",image3)

min_disp=16
num_disp=16*7
stereo=cv2.StereoBM_create(numDisparities=16*7, blockSize=21)

disparity = stereo.compute(image1, image2).astype(np.float32) / 16.0
disp_map = (disparity - min_disp)/num_disp 
print(" ")
print("The disparity map is :")
print(disp_map)


cv2.imwrite("task2_disparity.jpg",disparity)

