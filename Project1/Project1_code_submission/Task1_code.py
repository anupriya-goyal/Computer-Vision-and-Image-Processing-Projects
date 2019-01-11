
# coding: utf-8

# In[ ]:


#References:
#1.http://homepages.inf.ed.ac.uk/rbf/HIPR2/sobel.htm
#this link used to read about sobel edge detector
# Used to methods to do convolution to obatin edge detected images.
# 2nd method images are imcluded in report


# In[ ]:


# 2nd Method
import cv2
import math

#list for sobel operator 
g_sob_x = [[-1,0,1],[-2,0,2],[-1,0,1]]
g_sob_y = [[1,2,1],[0,0,0],[-1,-2,-1]]
original_img = cv2.imread("path/task1.png", 0)

x_matrix_sobel =original_img.copy()
#No. of rows in original image
rows= original_img.shape[0] 
#No. of columns in original image
columns = original_img.shape[1] 
xy_matrix_sobel=original_img.copy()
original_img[0,:] = original_img[:,0] = original_img[:,-1] = original_img[-1,:] = 0
#creating a copy of image to store edge detected image values      
y_matrix_sobel =original_img.copy()  

res1 =0
res2 =0

for i in range(1, 598):  
    for j in range (1,898):
       
        res1 = (  original_img[i-1][j-1]* g_sob_x[0][2]) +                (  original_img[i-1][j]* g_sob_x[0][1]) +                ( original_img[i-1][j+1]* g_sob_x[0][0] ) +                (original_img[i][j-1]* g_sob_x[1][2] ) +                (original_img[i][j]* g_sob_x[1][1] ) +                ( original_img[i][j+1]* g_sob_x[1][0] ) +                ( original_img[i+1][j-1]* g_sob_x[2][2]) +                (original_img[i+1][j]*g_sob_x[2][1]) +                ( original_img[i+1][j+1]* g_sob_x[2][0])
 
        res2 = (original_img[i-1][j-1]*g_sob_y[0][2]) +                ( original_img[i-1][j]*g_sob_y[0][1]) +                (original_img[i-1][j+1]*g_sob_y [0][0]) +                ( original_img[i][j-1]*g_sob_y [1][2] ) +                ( original_img[i][j]*g_sob_y [1][1]) +                ( original_img[i][j+1]*g_sob_y [1][0] ) +                ( original_img[i+1][j-1]*g_sob_y [2][2] ) +                (original_img[i+1][j]*g_sob_y [2][1] ) +                ( original_img[i+1][j+1]*g_sob_y [2][0] ) 
#vertical edges
        x_matrix_sobel[i-1][j-1] = res1
#horizontal edges
        y_matrix_sobel[i-1][j-1] = res2
#combining vertical and horizontal edges
        edge_magnitude =math.sqrt(res1 ** 2 + res2 ** 2)
        xy_matrix_sobel[i-1][j-1]=edge_magnitude
        
        #print(np.asarray(edge_x))
#print(sobelxImage)

#Eliminating zero values in vertical edges,horizontal edges and combined edges
max_of_y=0
min_of_y=0
for i in range(1, rows): 
     for j in range (1,columns):
         if(min_of_y> y_matrix_sobel[i-1][j-1]):
             min_of_y= y_matrix_sobel[i-1][j-1]  
         if(max_of_y< y_matrix_sobel[i-1][j-1]):
             max_of_y= y_matrix_sobel[i-1][j-1]
                
max_of_x=0
min_of_x=0
for i in range(1, rows): 
     for j in range (1,columns):
         if(min_of_x> x_matrix_sobel[i-1][j-1]):
             min_of_x= x_matrix_sobel[i-1][j-1] 
         if(max_of_x< x_matrix_sobel[i-1][j-1]):
             max_of_x= x_matrix_sobel[i-1][j-1]
max_of_xy=0
min_of_xy=0
for i in range(1, rows): 
     for j in range (1,columns):
         if(min_of_xy> xy_matrix_sobel[i-1][j-1]):
             min_of_xy= xy_matrix_sobel[i-1][j-1]
         if(max_of_xy< xy_matrix_sobel[i-1][j-1]):
             max_of_xy= xy_matrix_sobel[i-1][j-1]

x_dir_edge = (x_matrix_sobel -min_of_x) / math.fabs( max_of_x-min_of_x)
cv2.imshow('Edges of x direction',x_dir_edge)
print(x_dir_edge.shape)
y_dir_edge = (y_matrix_sobel -min_of_y) / math.fabs( max_of_y-min_of_y) 
cv2.imshow('Edges of y direction',y_dir_edge)
print(y_dir_edge.shape)
xy_comb_edge = (xy_matrix_sobel -min_of_xy) / math.fabs( max_of_xy-min_of_xy)   
cv2.imshow('Combined edges in x and y direction',xy_comb_edge)
print(xy_comb_edge.shape)
cv2.imwrite('x_dir_edge.png',x_dir_edge)
cv2.imwrite('y_dir_edge.png',y_dir_edge)
cv2.imwrite('xy_comb_edge.png',xy_comb_edge)


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[1]:


# 1 st method 
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
t_img = cv2.imread("C:/Users/Anupriya/Documents/task1.png", 0)

print(t_img.shape)
print(t_img.shape[0])
sobel=t_img.copy()
print(sobel)


# In[2]:


matrix = []
for i in range (3):
    matrix.append([])
    for j in range (3):
        matrix[i].append(0)
        
print(matrix)


# In[3]:


result = []
for i in range (600):
    result.append([])
    for j in range (900):
        result[i].append(0)
        

#print(result)


# In[5]:


matrix[0][0]=1
matrix[0][1]=0
matrix[0][2]=-1
matrix[1][0]=2
matrix[1][1]=0
matrix[1][2]=-2
matrix[2][0]=1
matrix[2][1]=0
matrix[2][2]=-1


# In[6]:


for i in range(598):
    for j in range(898):
        result[i][j]=((t_img[i][j]*matrix[0][0])+
                     (t_img[i][j+1]*matrix[0][1])+
                      (t_img[i][j+2]*matrix[0][2])+
                      (t_img[i+1][j]*matrix[1][0])+
                      (t_img[i+1][j+1]*matrix[1][1])+
                      (t_img[i+1][j+2]*matrix[1][2])+
                      (t_img[i+2][j]*matrix[2][0])+
                      (t_img[i+2][j+1]*matrix[2][1])+
                      (t_img[i+2][j+2]*matrix[2][2])
                      
                     
                     )


# In[9]:


plt.imshow(result,cmap='gray')


# In[19]:


matrix1 = []
for i in range (3):
    matrix1.append([])
    for j in range (3):
        matrix1[i].append(0)
        
print(matrix1)


# In[20]:


matrix1[0][0]=1
matrix1[0][1]=2
matrix1[0][2]=1
matrix1[1][0]=0
matrix1[1][1]=0
matrix1[1][2]=0
matrix1[2][0]=-1
matrix1[2][1]=-2
matrix1[2][2]=-1


# In[22]:


result1 = []
for i in range (600):
    result1.append([])
    for j in range (900):
        result1[i].append(0)
        


# In[23]:


for i in range(598):
    for j in range(898):
        result1[i][j]=((t_img[i][j]*matrix1[0][0])+
                     (t_img[i][j+1]*matrix1[0][1])+
                      (t_img[i][j+2]*matrix1[0][2])+
                      (t_img[i+1][j]*matrix1[1][0])+
                      (t_img[i+1][j+1]*matrix1[1][1])+
                      (t_img[i+1][j+2]*matrix1[1][2])+
                      (t_img[i+2][j]*matrix1[2][0])+
                      (t_img[i+2][j+1]*matrix1[2][1])+
                      (t_img[i+2][j+2]*matrix1[2][2])
                      
                     
                     )


# In[24]:


plt.imshow(result1,cmap='gray')


# In[25]:


# In[2]:


plt.imshow(result1,cmap='gray')


# In[3]:


plt.imshow(result,cmap='gray')

