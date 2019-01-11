
# coding: utf-8

# In[37]:


#Task2 Image segmentation and point detection 

#Histogram for point detection
import cv2
import numpy as np
import array 
from matplotlib import pyplot as plt 

img = cv2.imread("turbine-blade.jpg",0)
arr =[]

for i in range (0,256):
    count=0
    for p in range (0,img.shape[0]):
        for q in range (0,img.shape[1]):
            if img[p][q]==i:
                count=count+1
    arr.append(count)                
x = np.array([i for i in range(256)])     
a = np.array(arr)  
plt.bar(x, a, width=1, bottom=None, align='center', data=None)
plt.title("histogram") 
plt.show()

img = cv2.imread("turbine-blade.jpg",0)
mask = []
array1= []
array2=[]

#created mask 
mask =[[-0.25,-0.25 ,-0.25],[-0.25,2,-0.25],[-0.25,-0.25 ,-0.25]]
# choosing threshold on the basis of histogram and trial methods
T= 80
mask=np.array(mask)
img2=img.copy()
R=0
for i in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        R= ((mask[1][1]*img[i][j])+(mask[1][0]*img[i][j-1])+(mask[1][2]*img[i][j+1])+(mask[0][1]*img[i-1][j])+(mask[0][0]*img[i-1][j-1])+(mask[0][2]*img[i-1][j+1])+(mask[2][1]*img[i+1][j])+(mask[2][0]*img[i+1][j-1])+(mask[2][2]*img[i+1][j+1]))
        img2[i][j]=R
        if abs(R) >= T:
            
            img2[i][j]=255
        else:
            img2[i][j]=0
        
    
cv2.imwrite("point_detected.jpg",img2)


 
    







            
            
    
    

