
# coding: utf-8

# In[ ]:


#References:
#1.https://docs.opencv.org/3.4.0/d4/dc6/tutorial_py_template_matching.html
#2.https://docs.opencv.org/2.4/doc/tutorials/imgproc/histograms/template_matching/template_matching.html
#3.http://www.aishack.in/tutorials/template-matching/
#adopted methods to detect cursor using above links of references.
#used the way functions are defined in code from above links.
#for task3_bonus created three templates by cropping from the images given for finding three different cursor. Then used the below code #only to detect the cursor
#able to detect in the cursor in the images. To run code on different template and images give path of the template and image in the #variables t_img and img_pos


# In[ ]:



import cv2

#read image of template and resize it
t_img = cv2.imread('path/template.png')
t_img = cv2.resize(t_img , (0,0), fx=0.7, fy=0.7)
#read different images from the file and resize it
img_pos = cv2.imread('path/pos_1.jpg')
img_pos = cv2.resize(img_pos, (0,0), fx=0.9, fy=0.9) 
# convert into gray scale image
g_temp = cv2.cvtColor(t_img , cv2.COLOR_BGR2GRAY)
# Convert to grayscale image
g_img = cv2.cvtColor(img_pos, cv2.COLOR_BGR2GRAY)
# find the width and height of template
width=g_temp.shape[0]
height=g_temp.shape[1]

#sigma = 0.3*((3-1)*0.5 - 1) + 0.8
#gauss_res = cv2.GaussianBlur(img,(3,3),sigma)
#gauss_res = cv2.medianBlur(img,3)
#gauss_res = cv2.Laplacian(dst,cv2.CV_64F,0)
#gauss_template = cv2.Laplacian(template,cv2.CV_64F,0)
#result = cv2.matchTemplate(dst,dst_template,cv2.TM_CCOEFF_NORMED)
#Now,first blur the image with Gaussian Blur method and Second apply Laplacian
gauss_res = cv2.GaussianBlur(g_img,(3,3),0)
gauss_res = cv2.Laplacian(gauss_res,cv2.CV_32F,0)
gauss_temp_res = cv2.Laplacian(g_temp,cv2.CV_32F,0)
# the method used for template matching is cv2.TM_SQDIFF
k = cv2.matchTemplate(gauss_res,gauss_temp_res, cv2.TM_SQDIFF)
_,_,position,_ = cv2.minMaxLoc(k)
pos_right = (position[0] + width, position[1] + height)
cv2.rectangle(img_pos,position, pos_right,255,2)
#threshold = 0.8    
#loc = np.where( res >= threshold)

#for pt in zip(*loc[::-1]):
    #cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow("Image_result", img_pos)
cv2.waitKey(0)
cv2.destroyAllWindows() 

