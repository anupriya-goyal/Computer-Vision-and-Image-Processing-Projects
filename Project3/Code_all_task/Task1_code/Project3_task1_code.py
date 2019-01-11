
# coding: utf-8

# In[2]:


#Task1 Morphology image processing 
import cv2
import numpy as np
#reading the original image in grayscale
img = cv2.imread("noise.jpg",0)
# defining the structuring element
str_elm =[[255,255,255],[255,255,255],[255,255,255]]
str_elm=np.asarray(str_elm)
#implemention function for dilation 
def dilation(image):
        image1 = image.copy()    
        for i in range (1,image.shape[0]-1):
            for j in range (1,image.shape[1]-1):
               
                if image[i][j]==255 or image[i][j-1]==255 or image[i][j+1]==255 or image[i-1][j]==255 or image[i-1][j-1]==255 or image[i-1][j+1]==255 or image[i+1][j]==255 or image[i+1][j-1]==255 or image[i+1][j+1]==255:
                    image1[i][j]=255
                    
                else:
                    image1[i][j]=0
                    
                
        return image1

    
#implemention function for erosion    
def erosion(image2):
            image3 = image2.copy() 
            
            
            for i in range (1,image2.shape[0]-1):
                for j in range (1,image2.shape[1]-1):
                    
                    if  image2[i][j]==255 and image2[i][j-1]==255 and image2[i][j+1]==255 and image2[i-1][j]==255 and image2[i-1][j-1]==255 and image2[i-1][j+1]==255 and image2[i+1][j]==255 and image2[i+1][j-1]==255 and image2[i+1][j+1]==255:
                            image3[i][j]=255
                                    

                    else:

                            image3[i][j]=0
                       

            return image3

#Algo1: Applying closing operation (dilation followed by erosion) and performing erosion again to remove noise from image 
img1=dilation(img)
cv2.imwrite("dilation_cl1.jpg",img1)
img2=erosion(img1)
cv2.imwrite("erosion_cl1.jpg",img2)
img3=erosion(img2)
cv2.imwrite("res_noise1.jpg",img3)
#Extracting boundaries from res_noise1.jpg
img4=erosion(img3)
img5=img3-img4
cv2.imwrite("res_bound1.jpg",img5)


#Ago2: Applying opening operation (erosion followed by dilation) and performing dilation again to remove noise from image 

img6=erosion(img)
cv2.imwrite("erosion_op1.jpg",img6)
img7=dilation(img6)
cv2.imwrite("dilation_op1.jpg",img7)
img8=dilation(img7)
cv2.imwrite("res_noise2.jpg",img8)
#Extracting boundaries from res_noise1.jpg
img9=erosion(img8)
img10=img8-img9
cv2.imwrite("res_bound2.jpg",img10)


