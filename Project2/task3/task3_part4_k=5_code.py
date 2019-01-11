
# coding: utf-8

# In[ ]:


UBIT =  'anupriya'; 
import numpy as np; 
np.random.seed(sum([ord(c) for c in UBIT]))

import cv2
import math
#np.seterr(over='ignore')

# Load an color image in grayscale
img = cv2.imread("baboon.jpg")
centroid = np.array([[[img[0][0][0],img[0][0][1],img[0][0][2]],[img[0][1][0],img[0][1][1],img[0][1][2]],[img[0][2][0],img[0][2][1],img[0][2][2]],[img[0][3][0],img[0][3][1],img[0][3][2]],[img[0][4][0],img[0][4][1],img[0][4][2]]]])

iterate=0
while iterate<=21:
    
    distance =[] 
    cluster1 =[]
    cluster2 =[]
    cluster3= []
    cluster4= []
    cluster5= []
    
    cluster1_xy_values=[]
    cluster2_xy_values=[]
    cluster3_xy_values=[]
    cluster4_xy_values=[]
    cluster5_xy_values=[]
    m=0
    n=0
    r=0
    i=0
    j=0
    h=0
    img_c=0
    img_r=0
    index=0
    
    #print(img[m][n][r+2])


    
    while img_r<=511:
        img_c=0
        n=0
        while img_c<=511:
            for j in range(5):
                distance.append(math.sqrt(((int(img[m][n][r])-int(centroid[i][j][h]))**2)+((int(img[m][n][r+1])-int(centroid[i][j][h+1]))**2)+((int(img[m][n][r+2])-int(centroid[i][j][h+2]))**2)))
    
                
            
            a=min(distance[index],distance[index+1],distance[index+2],distance[index+3],distance[index+4])
            for p in range(index,index+5):
                if a==distance[p]:
                    ind_match=p
            
            if ind_match ==index:
                cluster1.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster1_xy_values.append([m , n])
            if ind_match==index+1:
                cluster2.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster2_xy_values.append([m, n])
            if ind_match==index+2:
                cluster3.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster3_xy_values.append([m , n])
            if ind_match==index+3:
                cluster4.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster4_xy_values.append([m , n])
            if ind_match==index+4:
                cluster5.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster5_xy_values.append([m , n])
            
            
            #print(cluster1)
            #print(cluster2)
            #print(cluster3)
            n=n+1
            #print("value of n is",n)
            img_c=img_c+1
            index=index+5
        m=m+1
        img_r=img_r+1
  
    #new_centers_find
    #print(len(cluster1))
    new_center1 =[]
    j=0
    sum_x=0
    for i in range(len(cluster1)):
        sum_x=cluster1[i][j]+sum_x
        
    new_center1.append((sum_x)/(len(cluster1)))
    #print(new_center1)
    j=0
    sum_y=0
    for i in range(len(cluster1)):
        sum_y=cluster1[i][j+1]+sum_y
        
    a=((sum_y)/(len(cluster1)))
    new_center1.append(a)
    #print(new_center1)
    
    z=0
    sum_z=0
    for i in range(len(cluster1)):
        sum_z=cluster1[i][z+2]+sum_z
    
    a=((sum_z)/(len(cluster1)))
    new_center1.append(a)
    #print(new_center1)
    
    #new_centers_find
    #print(len(cluster2))
    new_center2 =[]
    j=0
    sum_x=0
    for i in range(len(cluster2)):
        sum_x=cluster2[i][j]+sum_x
    
    new_center2.append((sum_x)/(len(cluster2)))
    #print(new_center2)
    
    j=0
    sum_y=0
    for i in range(len(cluster2)):
        sum_y=cluster2[i][j+1]+sum_y
    
    a=((sum_y)/(len(cluster2)))
    new_center2.append(a)
    #print(new_center2)
    
    z=0
    sum_z=0
    for i in range(len(cluster2)):
        sum_z=cluster2[i][z+2]+sum_z
        
    a=((sum_z)/(len(cluster2)))
    new_center2.append(a)
    #print(new_center2)
    
    #new_centers_find
    #print(len(cluster3))
    new_center3 =[]
    j=0
    sum_x=0
    for i in range(len(cluster3)):
        sum_x=cluster3[i][j]+sum_x
    new_center3.append((sum_x)/(len(cluster3)))
    #print(new_center3)
    
    j=0
    sum_y=0
    for i in range(len(cluster3)):
         sum_y=cluster3[i][j+1]+sum_y
    
    a=((sum_y)/(len(cluster3)))
    new_center3.append(a)
    #print(new_center3)
    
    z=0
    sum_z=0
    for i in range(len(cluster3)):
            sum_z=cluster3[i][z+2]+sum_z
    a=((sum_z)/(len(cluster3)))
    new_center3.append(a)
    #print(new_center3)  
    
    new_center4 =[]
    j=0
    sum_x=0
    for i in range(len(cluster4)):
        sum_x=cluster4[i][j]+sum_x
        
    new_center4.append((sum_x)/(len(cluster4)))
    #print(new_center4)
    j=0
    sum_y=0
    for i in range(len(cluster4)):
        sum_y=cluster4[i][j+1]+sum_y
        
    a=((sum_y)/(len(cluster4)))
    new_center4.append(a)
    #print(new_center4)
    
    z=0
    sum_z=0
    for i in range(len(cluster4)):
        sum_z=cluster4[i][z+2]+sum_z
    
    a=((sum_z)/(len(cluster4)))
    new_center4.append(a)
    #print(new_center4)
    
    new_center5 =[]
    j=0
    sum_x=0
    for i in range(len(cluster5)):
        sum_x=cluster5[i][j]+sum_x
        
    new_center5.append((sum_x)/(len(cluster5)))
    #print(new_center5)
    j=0
    sum_y=0
    for i in range(len(cluster5)):
        sum_y=cluster5[i][j+1]+sum_y
        
    a=((sum_y)/(len(cluster5)))
    new_center5.append(a)
    #print(new_center1)
    
    z=0
    sum_z=0
    for i in range(len(cluster5)):
        sum_z=cluster5[i][z+2]+sum_z
    
    a=((sum_z)/(len(cluster5)))
    new_center5.append(a)
    #print(new_center1)
    
    
    
    
    center_array = [[new_center1,new_center2 ,new_center3,new_center4,new_center5 ]]
    np.array(center_array)
    centroid = center_array
    #print(centroid)

    iterate=iterate+1
final_cluster1_xy_values=[cluster1_xy_values]
final_cluster1_xy_values=np.array(final_cluster1_xy_values)

for i in range(len(final_cluster1_xy_values[0])):
    a=final_cluster1_xy_values[0][i][0]
    b=final_cluster1_xy_values[0][i][1]
    img[a][b]=center_array[0][0]

final_cluster2_xy_values=[cluster2_xy_values]
final_cluster2_xy_values=np.array(final_cluster2_xy_values)

for i in range(len(final_cluster2_xy_values[0])):
    a=final_cluster2_xy_values[0][i][0]
    b=final_cluster2_xy_values[0][i][1]
    img[a][b]=center_array[0][1]
    
final_cluster3_xy_values=[cluster3_xy_values]
final_cluster3_xy_values=np.array(final_cluster3_xy_values)
for i in range(len(final_cluster3_xy_values[0])):
    a=final_cluster3_xy_values[0][i][0]
    b=final_cluster3_xy_values[0][i][1]
    img[a][b]=center_array[0][2]

final_cluster4_xy_values=[cluster4_xy_values]
final_cluster4_xy_values=np.array(final_cluster4_xy_values)
for i in range(len(final_cluster4_xy_values[0])):
    a=final_cluster4_xy_values[0][i][0]
    b=final_cluster4_xy_values[0][i][1]
    img[a][b]=center_array[0][3]

final_cluster5_xy_values=[cluster5_xy_values]
final_cluster5_xy_values=np.array(final_cluster5_xy_values)
for i in range(len(final_cluster5_xy_values[0])):
    a=final_cluster5_xy_values[0][i][0]
    b=final_cluster5_xy_values[0][i][1]
    img[a][b]=center_array[0][4]

cv2.imwrite("task3_part4_k5.jpg",img)
    
                   
            
        
    

