
# coding: utf-8

# In[9]:


UBIT =  'anupriya'; 
import numpy as np; 
np.random.seed(sum([ord(c) for c in UBIT]))
#task1 code for all parts
import cv2

#read the two images of mountains and convert it to grayscale images  
#provide the path to read image

image1 = cv2.imread("mountain1.jpg",0)
image2 = cv2.imread("mountain2.jpg",0)


sift = cv2.xfeatures2d.SIFT_create()
#detecting keypoints
keypoint1, d1 = sift.detectAndCompute(image1,None)
keypoint2, d2 = sift.detectAndCompute(image2,None)


#drawing keypoints on both images

img_key1=cv2.drawKeypoints(image1,keypoint1,None)
img_key2=cv2.drawKeypoints(image2,keypoint2,None)


# BFMatcher with default params
burteforce_matcher = cv2.BFMatcher()
total_matches = burteforce_matcher.knnMatch(d1,d2, k=2)

# Apply ratio test
good_points = []

for m,n in total_matches:
    if m.distance < 0.75*n.distance:
        good_points.append([m])
        
    
# cv2.drawMatchesKnn expects list of lists as matches.
image_knn = cv2.drawMatchesKnn(image1,keypoint1,image2,keypoint2,good_points,None,flags=2)

#saving images at particular location.Provide path to view the image at location

cv2.imwrite('task1_sift1.jpg',img_key1)
cv2.imwrite('task1_sift2.jpg',img_key2)
cv2.imwrite("task1_matches_knn.jpg",image_knn)
#task1 part3 computing homography matrix H

FLANN_INDEX_KDTREE = 0
inx_parameter = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
srch_parameter = dict(checks = 50)

dect_flann = cv2.FlannBasedMatcher(inx_parameter, srch_parameter )

matches_by_flann = dect_flann.knnMatch(d1,d2,k=2)

# store all the good matches as per Lowe's ratio test.
matched_good_points = []
for m,n in matches_by_flann:
    if m.distance < 0.75*n.distance:
        matched_good_points.append(m)

RANDOM_MATCHES_COUNT= 10
if len(matched_good_points)>RANDOM_MATCHES_COUNT:
    source_points = np.float32([ keypoint1[m.queryIdx].pt for m in matched_good_points ]).reshape(-1,1,2)
    destination_points = np.float32([ keypoint2[m.trainIdx].pt for m in matched_good_points ]).reshape(-1,1,2)
    
    #finding homography matrix H
    H, mask = cv2.findHomography(source_points ,destination_points, cv2.RANSAC,5.0)
    #printing homography matrix H
    print(H)
    matchesMask = mask.ravel().tolist()

    h,w = image1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,H)
   
    #image2 = cv2.polylines(image2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
     
#drawing 10 random matches using only inliers
draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

image3 = cv2.drawMatches(image1,keypoint1,image2,keypoint2,matched_good_points,None,**draw_params)

cv2.imwrite("task1_matches.jpg",image3)

image4 = cv2.imread("mountain2.jpg",0)
#task1 part5 warping
r1, c1 = image1.shape[:2]
r2, c2 = image4.shape[:2]

points_from_1 = np.float32([[0,0], [0,r1], [c1, r1], [c1,0]]).reshape(-1,1,2)
pts = np.float32([[0,0], [0,r2], [c2, r2], [c2,0]]).reshape(-1,1,2)

points_from_2 = cv2.perspectiveTransform(pts, H)
pts_list = np.concatenate((points_from_1, points_from_2), axis=0)

[minimum_x, minimum_y] = np.int32(pts_list.min(axis=0).ravel() - 0.5)
[maximum_x, maximum_y] = np.int32(pts_list.max(axis=0).ravel() + 0.5)

d_trans = [-minimum_x, -minimum_y]
trans_Homo = np.array([[1, 0, d_trans[0]], [0, 1, d_trans[1]], [0,0,1]])

result_image = cv2.warpPerspective(image1, trans_Homo.dot(H), (maximum_x - minimum_x, maximum_y - minimum_y))
result_image[d_trans[1]:r1+d_trans[1],d_trans[0]:c1+d_trans[0]] = image4
cv2.imwrite("task1_pano.jpg",result_image)
        
#References for task1:
#1.https://docs.opencv.org/3.4/da/df5/tutorial_py_sift_intro.html
#2.https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html
#3.https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_feature_homography/py_feature_homography.html
#4.https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_feature_homography/py_feature_homography.html
#5.https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_calib3d/py_depthmap/py_depthmap.html
#6.https://www.kaggle.com/asymptote/homography-estimate-stitching-two-imag/code



