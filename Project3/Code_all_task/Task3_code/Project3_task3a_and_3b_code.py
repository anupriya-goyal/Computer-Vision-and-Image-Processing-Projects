
# coding: utf-8

# In[9]:


import cv2
import numpy as np
import math



def hough_trans(image):
    w = image.shape[0]
    h = image.shape[1]
    y_nzv, x_nzv = np.nonzero(image)
   
    angle = np.deg2rad(np.arange(-90.0, 90.0))
    cos_value = np.cos(angle)
    sin_value = np.sin(angle)
    total_angles= len(angle)
   
    length_diagonal = int(np.ceil(np.sqrt(w * w + h * h)))
    
    
    value_acc = np.zeros((2 * length_diagonal, total_angles),dtype=np.uint64)
    values = np.linspace(-length_diagonal, length_diagonal, length_diagonal * 2.0)
    
    for i in range(len(x_nzv)):
        x=x_nzv[i]
        y=y_nzv[i]
        
        for t in range(total_angles):
            value=int(round(x * cos_value[t] + y * sin_value[t]) + length_diagonal)
            value_acc[value,t]+=1
            

    return value_acc, angle, values

#edge detection method using sobel



original_img_1 = cv2.imread("hough.jpg")

#list for sobel operator 
g_sob_x = [[-1,0,1],[-2,0,2],[-1,0,1]]
g_sob_y = [[1,2,1],[0,0,0],[-1,-2,-1]]
original_img = cv2.imread("hough.jpg", 0)

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

for i in range(1,original_img.shape[0]-1 ):  
    for j in range (1,original_img.shape[1]-1):
       
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

xy_comb_edge = (xy_matrix_sobel -min_of_xy) / math.fabs( max_of_xy-min_of_xy)   

for i in range (xy_matrix_sobel.shape[0]):
        for j in range(xy_matrix_sobel.shape[1]):
            if xy_matrix_sobel[i][j] > 115:
                
                xy_matrix_sobel[i][j] = 255         
            else:
                
                xy_matrix_sobel[i][j] = 0


value_acc, angle, values = hough_trans(xy_matrix_sobel)
count=0
for i in range(len(values)):
    for j in range(len(angle)):
        if(value_acc[i][j]>150):
            
            a = np.cos(angle[j])
            b = np.sin(angle[j])
            x0 = a*values[i]
            y0 = b*values[i]
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            angle1=np.arctan2(y2-y1,x2-x1)*(180.0)/(np.pi)
            count=count+1
            if(angle1<=-90.00 and angle1>-93):
                cv2.line(original_img_1,(x1,y1),(x2,y2),(0,255,0),1)
                
                      
            else:
                cv2.line(original_img_1,(x1,y1),(x2,y2),(255,255,255),1)
                    
            

cv2.imwrite("red_blue_line.jpg",original_img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()



