
# coding: utf-8

# In[ ]:


#Task2 Part2b Segmentation of image
import cv2
import numpy as np
import array 
from matplotlib import pyplot as plt 

img = cv2.imread("segment.jpg",0)
arr =[]
#Plotting histogram
for i in range (0,256):
    count=0
    for p in range (img.shape[0]):
        for q in range (img.shape[1]):
            if img[p][q]==i:
                count=count+1
    arr.append(count)                
x = np.array([i for i in range(256)])     
a = np.array(arr)  
plt.bar(x, a, width=1, bottom=None, align='center', data=None)
plt.title("histogram") 
plt.show()    

img1 = cv2.imread("segment.jpg",0)

#function to determine threshold value
def threshold_calculate(img,threshold,T0):
    G1=[]
    G2=[]
    pixel_sum1=0
    pixel_sum2=0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j]>threshold:
                G1.append(img[i][j])
            else:
                G2.append(img[i][j])
   
    
    for i in range (len(G1)):
        pixel_sum1=pixel_sum1+G1[i]
    
    if(len(G1) != 0):
        avg1=(pixel_sum1)/(len(G1))
    else:
        avg1 = 0
    for j in range (len(G2)):
        pixel_sum2=pixel_sum2+G2[j]
    
    avg2=(pixel_sum2)/(len(G2))
    
    new_threshold=(0.5)*(avg1+avg2)
    
    
    if abs(new_threshold-threshold) >T0:
        threshold_calculate(img,new_threshold,T0)
    
    return new_threshold

new_threshold=threshold_calculate(img1,254,18)
new_threshold =198.5


img2=img1.copy()
    
for i in range (img1.shape[0]):
    for j in range (img1.shape[1]):
        if img1[i][j]>=new_threshold:
            img2[i][j]=255
            
        else:
            img2[i][j]=0
            
cv2.imwrite("segment.jpg",img2)


        

