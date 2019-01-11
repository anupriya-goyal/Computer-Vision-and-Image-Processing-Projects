
# coding: utf-8

# In[ ]:


UBIT =  'anupriya'; 
import numpy as np; 
np.random.seed(sum([ord(c) for c in UBIT]))

import cv2
import math



img = cv2.imread("baboon.jpg")
centroid = np.array([[[img[0][0][0],img[0][0][1],img[0][0][2]],[img[0][1][0],img[0][1][1],img[0][1][2]],[img[0][2][0],img[0][2][1],img[0][2][2]],[img[0][3][0],img[0][3][1],img[0][3][2]],[img[0][4][0],img[0][4][1],img[0][4][2]],[img[0][5][0],img[0][5][1],img[0][5][2]],[img[0][6][0],img[0][6][1],img[0][6][2]],[img[0][7][0],img[0][7][1],img[0][7][2]],[img[0][8][0],img[0][8][1],img[0][8][2]],[img[0][9][0],img[0][9][1],img[0][9][2]],[img[0][10][0],img[0][10][1],img[0][10][2]],[img[0][11][0],img[0][11][1],img[0][11][2]],[img[0][12][0],img[0][12][1],img[0][12][2]],[img[0][13][0],img[0][13][1],img[0][13][2]],[img[0][14][0],img[0][14][1],img[0][14][2]],[img[0][15][0],img[0][15][1],img[0][15][2]],[img[0][16][0],img[0][16][1],img[0][16][2]],[img[0][17][0],img[0][17][1],img[0][17][2]],[img[0][18][0],img[0][18][1],img[0][18][2]],[img[0][19][0],img[0][19][1],img[0][19][2]]]])

iterate=0
while iterate<=50:
    
    distance =[] 
    cluster1 =[]
    cluster2 =[]
    cluster3= []
    cluster4= []
    cluster5= []
    cluster6= []
    cluster7= []
    cluster8= []
    cluster9= []
    cluster10= []
    cluster11 =[]
    cluster12 =[]
    cluster13= []
    cluster14= []
    cluster15= []
    cluster16= []
    cluster17= []
    cluster18= []
    cluster19= []
    cluster20= []
    
    cluster1_xy_values=[]
    cluster2_xy_values=[]
    cluster3_xy_values=[]
    cluster4_xy_values=[]
    cluster5_xy_values=[]
    cluster6_xy_values=[]
    cluster7_xy_values=[]
    cluster8_xy_values=[]
    cluster9_xy_values=[]
    cluster10_xy_values=[]
    cluster11_xy_values=[]
    cluster12_xy_values=[]
    cluster13_xy_values=[]
    cluster14_xy_values=[]
    cluster15_xy_values=[]
    cluster16_xy_values=[]
    cluster17_xy_values=[]
    cluster18_xy_values=[]
    cluster19_xy_values=[]
    cluster20_xy_values=[]
    
    m=0
    n=0
    r=0
    i=0
    j=0
    h=0
    img_c=0
    img_r=0
    index=0
    
    while img_r<=511:
        img_c=0
        n=0
        while img_c<=511:
            for j in range(20):
                distance.append(math.sqrt(((int(img[m][n][r])-int(centroid[i][j][h]))**2)+((int(img[m][n][r+1])-int(centroid[i][j][h+1]))**2)+((int(img[m][n][r+2])-int(centroid[i][j][h+2]))**2)))
            
            a=min(distance[index],distance[index+1],distance[index+2],distance[index+3],distance[index+4],distance[index+5],distance[index+6],distance[index+7],distance[index+8],distance[index+9],distance[index+10],distance[index+11],distance[index+12],distance[index+13],distance[index+14],distance[index+15],distance[index+16],distance[index+17],distance[index+18],distance[index+19])
            for p in range(index,index+20):
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
            if ind_match==index+5:
                cluster6.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster6_xy_values.append([m , n])
            if ind_match==index+6:
                cluster7.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster7_xy_values.append([m , n])
            if ind_match==index+7:
                cluster8.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster8_xy_values.append([m , n])
            if ind_match==index+8:
                cluster9.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster9_xy_values.append([m , n])
            if ind_match==index+9:
                cluster10.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster10_xy_values.append([m , n])
            if ind_match==index+10:
                cluster11.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster11_xy_values.append([m , n])
            if ind_match==index+11:
                cluster12.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster12_xy_values.append([m , n])
            if ind_match==index+12:
                cluster13.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster13_xy_values.append([m , n])
            if ind_match==index+13:
                cluster14.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster14_xy_values.append([m , n])
            if ind_match==index+14:
                cluster15.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster15_xy_values.append([m , n])
            if ind_match==index+15:
                cluster16.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster16_xy_values.append([m , n])
            if ind_match==index+16:
                cluster17.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster17_xy_values.append([m , n])
            if ind_match==index+17:
                cluster18.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster18_xy_values.append([m , n])
            if ind_match==index+18:
                cluster19.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster19_xy_values.append([m , n])
            if ind_match==index+19:
                cluster20.append([img[m][n][r],img[m][n][r+1],img[m][n][r+2]])
                cluster20_xy_values.append([m , n])
                
            #print(cluster1)
            #print(cluster2)
            #print(cluster3)
            n=n+1
            #print("value of n is",n)
            img_c=img_c+1
            index=index+10
        m=m+1
        img_r=img_r+1
  
    #new_centers_find
    #print(len(cluster1))
    new_center1 =[]
    
    if len(cluster1) > 0:
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
    else:
        new_center1=[0,0,0]
        
    new_center2 =[]
    if len(cluster2) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster2)):
                 sum_x=cluster2[i][j]+sum_x
        
            new_center2.append((sum_x)/(len(cluster2)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster2)):
                sum_y=cluster2[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster2)))
            new_center2.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster2)):
                sum_z=cluster2[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster2)))
            new_center2.append(a)
    #print(new_center1)
    else:
        new_center2=[0,0,0]
    new_center3 =[]
    if len(cluster3) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster3)):
                 sum_x=cluster3[i][j]+sum_x
        
            new_center3.append((sum_x)/(len(cluster3)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster3)):
                sum_y=cluster3[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster3)))
            new_center3.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster3)):
                sum_z=cluster3[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster3)))
            new_center3.append(a)
    #print(new_center1)
    else:
        new_center3=[0,0,0]
    
    new_center4 =[]
    if len(cluster4) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster4)):
                 sum_x=cluster4[i][j]+sum_x
        
            new_center4.append((sum_x)/(len(cluster4)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster4)):
                sum_y=cluster4[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster4)))
            new_center4.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster4)):
                sum_z=cluster4[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster4)))
            new_center4.append(a)
    #print(new_center1)
    else:
        new_center4=[0,0,0]
    
    new_center5 =[]
    
    if len(cluster5) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster5)):
                 sum_x=cluster5[i][j]+sum_x
        
            new_center5.append((sum_x)/(len(cluster5)))
    #print(new_center1)
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
    else:
        new_center5=[0,0,0]
        
    new_center6 =[]
    if len(cluster6) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster6)):
                 sum_x=cluster6[i][j]+sum_x
        
            new_center6.append((sum_x)/(len(cluster6)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster6)):
                sum_y=cluster6[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster6)))
            new_center6.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster6)):
                sum_z=cluster6[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster6)))
            new_center6.append(a)
    #print(new_center1)
    else:
        new_center6=[0,0,0]
   
    
    
    
    new_center7 =[]
    if len(cluster7) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster7)):
                 sum_x=cluster7[i][j]+sum_x
        
            new_center7.append((sum_x)/(len(cluster7)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster7)):
                sum_y=cluster7[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster7)))
            new_center7.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster7)):
                sum_z=cluster7[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster7)))
            new_center7.append(a)
    #print(new_center1)
    else:
        new_center7=[0,0,0]
    
    new_center8 =[]
    if len(cluster8) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster8)):
                 sum_x=cluster8[i][j]+sum_x
        
            new_center8.append((sum_x)/(len(cluster8)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster8)):
                sum_y=cluster8[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster8)))
            new_center8.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster8)):
                sum_z=cluster8[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster8)))
            new_center8.append(a)
    #print(new_center1)
    else:
        new_center8=[0,0,0]
    
    new_center9 =[]
    if len(cluster9)>0:
        
            j=0
            sum_x=0
            for i in range(len(cluster9)):
                sum_x=cluster9[i][j]+sum_x
        
            new_center9.append((sum_x)/(len(cluster9)))
            #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster9)):
                 sum_y=cluster9[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster9)))
            new_center9.append(a)
             #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster9)):
                    sum_z=cluster9[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster9)))
            new_center9.append(a)
    
    else:
        new_center9=[0,0,0]
    #print(new_center1)
    
    #new_center10 =[]
    #j=0
    #sum_x=0
    #for i in range(len(cluster10)):
        #sum_x=cluster10[i][j]+sum_x
        
    #new_center10.append((sum_x)/(len(cluster10)))
    
    #print(new_center1)
    #j=0
    #sum_y=0
    #for i in range(len(cluster10)):
        #sum_y=cluster10[i][j+1]+sum_y
        
    #a=((sum_y)/(len(cluster10)))
    #new_center10.append(a)
    #print(new_center1)
    
    #z=0
    #sum_z=0
    #for i in range(len(cluster10)):
        #sum_z=cluster10[i][z+2]+sum_z
    
    #a=((sum_z)/(len(cluster10)))
    #new_center10.append(a)
    #print(new_center1)
    img1 = cv2.imread("baboon.jpg")
    new_center10 =[]
    if len(cluster10) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster10)):
                 sum_x=cluster10[i][j]+sum_x
        
            new_center10.append((sum_x)/(len(cluster10)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster10)):
                sum_y=cluster10[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster10)))
            new_center10.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster10)):
                sum_z=cluster10[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster10)))
            new_center10.append(a)
    #print(new_center1)
    else:
        new_center10=[0,0,0]
    
    #new_centers_find
    #print(len(cluster1))
    new_center11 =[]
    
    if len(cluster11) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster11)):
                 sum_x=cluster11[i][j]+sum_x
        
            new_center11.append((sum_x)/(len(cluster11)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster11)):
                sum_y=cluster11[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster11)))
            new_center11.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster11)):
                sum_z=cluster11[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster11)))
            new_center11.append(a)
    #print(new_center1)
    else:
        new_center11=[0,0,0]
        
    new_center12 =[]
    if len(cluster12) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster12)):
                 sum_x=cluster12[i][j]+sum_x
        
            new_center12.append((sum_x)/(len(cluster12)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster12)):
                sum_y=cluster12[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster12)))
            new_center12.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster12)):
                sum_z=cluster12[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster12)))
            new_center12.append(a)
    #print(new_center1)
    else:
        new_center12=[0,0,0]
        
    new_center13 =[]
    if len(cluster13) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster13)):
                 sum_x=cluster13[i][j]+sum_x
        
            new_center13.append((sum_x)/(len(cluster13)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster13)):
                sum_y=cluster13[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster13)))
            new_center13.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster13)):
                sum_z=cluster13[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster13)))
            new_center13.append(a)
    #print(new_center1)
    else:
        new_center13=[0,0,0]
    
    new_center14 =[]
    if len(cluster14) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster14)):
                 sum_x=cluster14[i][j]+sum_x
        
            new_center14.append((sum_x)/(len(cluster14)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster14)):
                sum_y=cluster14[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster14)))
            new_center14.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster14)):
                sum_z=cluster14[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster14)))
            new_center14.append(a)
    #print(new_center1)
    else:
        new_center14=[0,0,0]
    
    new_center15 =[]
    
    if len(cluster15) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster15)):
                 sum_x=cluster15[i][j]+sum_x
        
            new_center15.append((sum_x)/(len(cluster15)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster15)):
                sum_y=cluster15[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster15)))
            new_center15.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster15)):
                sum_z=cluster15[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster15)))
            new_center15.append(a)
    #print(new_center1)
    else:
        new_center15=[0,0,0]
        
    new_center16 =[]
    if len(cluster16) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster16)):
                 sum_x=cluster16[i][j]+sum_x
        
            new_center16.append((sum_x)/(len(cluster16)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster16)):
                sum_y=cluster16[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster16)))
            new_center16.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster16)):
                sum_z=cluster16[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster16)))
            new_center16.append(a)
    #print(new_center1)
    else:
        new_center16=[0,0,0]
   
    
    
    
    new_center17 =[]
    if len(cluster17) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster17)):
                 sum_x=cluster17[i][j]+sum_x
        
            new_center17.append((sum_x)/(len(cluster17)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster17)):
                sum_y=cluster17[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster17)))
            new_center17.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster17)):
                sum_z=cluster17[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster17)))
            new_center17.append(a)
    #print(new_center1)
    else:
        new_center17=[0,0,0]
    
    new_center18 =[]
    if len(cluster18) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster18)):
                 sum_x=cluster18[i][j]+sum_x
        
            new_center18.append((sum_x)/(len(cluster18)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster18)):
                sum_y=cluster18[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster18)))
            new_center18.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster18)):
                sum_z=cluster18[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster18)))
            new_center18.append(a)
    #print(new_center1)
    else:
        new_center18=[0,0,0]
    
    new_center19 =[]
    if len(cluster19)>0:
        
            j=0
            sum_x=0
            for i in range(len(cluster19)):
                sum_x=cluster19[i][j]+sum_x
        
            new_center19.append((sum_x)/(len(cluster19)))
            #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster19)):
                 sum_y=cluster19[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster19)))
            new_center19.append(a)
             #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster19)):
                    sum_z=cluster19[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster19)))
            new_center19.append(a)
    
    else:
        new_center19=[0,0,0]
    #print(new_center1)
    
    #new_center10 =[]
    #j=0
    #sum_x=0
    #for i in range(len(cluster10)):
        #sum_x=cluster10[i][j]+sum_x
        
    #new_center10.append((sum_x)/(len(cluster10)))
    #print(new_center1)
    #j=0
    #sum_y=0
    #for i in range(len(cluster10)):
        #sum_y=cluster10[i][j+1]+sum_y
        
    #a=((sum_y)/(len(cluster10)))
    #new_center10.append(a)
    #print(new_center1)
    
    #z=0
    #sum_z=0
    #for i in range(len(cluster10)):
        #sum_z=cluster10[i][z+2]+sum_z
    
    #a=((sum_z)/(len(cluster10)))
    #new_center10.append(a)
    #print(new_center1)
    new_center20 =[]
    if len(cluster20) > 0:
            j=0
            sum_x=0
            for i in range(len(cluster20)):
                 sum_x=cluster20[i][j]+sum_x
        
            new_center20.append((sum_x)/(len(cluster20)))
    #print(new_center1)
            j=0
            sum_y=0
            for i in range(len(cluster20)):
                sum_y=cluster20[i][j+1]+sum_y
        
            a=((sum_y)/(len(cluster20)))
            new_center20.append(a)
    #print(new_center1)
    
            z=0
            sum_z=0
            for i in range(len(cluster20)):
                sum_z=cluster20[i][z+2]+sum_z
    
            a=((sum_z)/(len(cluster20)))
            new_center20.append(a)
    #print(new_center1)
    else:
        new_center20=[0,0,0]
    
    
    
    
    center_array = [[new_center1,new_center2 ,new_center3,new_center4,new_center5,new_center6,new_center7,new_center8,new_center9,new_center10,new_center11,new_center12,new_center13,new_center14,new_center15,new_center16,new_center17,new_center18,new_center19,new_center20]]
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

final_cluster6_xy_values=[cluster6_xy_values]
final_cluster6_xy_values=np.array(final_cluster6_xy_values)

for i in range(len(final_cluster6_xy_values[0])):
    a=final_cluster6_xy_values[0][i][0]
    b=final_cluster6_xy_values[0][i][1]
    img[a][b]=center_array[0][5]

final_cluster7_xy_values=[cluster7_xy_values]
final_cluster7_xy_values=np.array(final_cluster7_xy_values)
for i in range(len(final_cluster7_xy_values[0])):
    a=final_cluster7_xy_values[0][i][0]
    b=final_cluster7_xy_values[0][i][1]
    img[a][b]=center_array[0][6]
    
final_cluster8_xy_values=[cluster8_xy_values]
final_cluster8_xy_values=np.array(final_cluster8_xy_values)
for i in range(len(final_cluster8_xy_values[0])):
    a=final_cluster8_xy_values[0][i][0]
    b=final_cluster8_xy_values[0][i][1]
    img[a][b]=center_array[0][7]

final_cluster9_xy_values=[cluster9_xy_values]
final_cluster9_xy_values=np.array(final_cluster9_xy_values)
for i in range(len(final_cluster9_xy_values[0])):
    a=final_cluster9_xy_values[0][i][0]
    b=final_cluster9_xy_values[0][i][1]
    img[a][b]=center_array[0][8]

final_cluster10_xy_values=[cluster10_xy_values]
final_cluster10_xy_values=np.array(final_cluster10_xy_values)

for i in range(len(final_cluster10_xy_values[0])):
    a=final_cluster10_xy_values[0][i][0]
    b=final_cluster10_xy_values[0][i][1]
    img[a][b]=center_array[0][9]

final_cluster11_xy_values=[cluster11_xy_values]
final_cluster11_xy_values=np.array(final_cluster11_xy_values)

for i in range(len(final_cluster11_xy_values[0])):
    a=final_cluster11_xy_values[0][i][0]
    b=final_cluster11_xy_values[0][i][1]
    img[a][b]=center_array[0][10]
    
final_cluster12_xy_values=[cluster12_xy_values]
final_cluster12_xy_values=np.array(final_cluster12_xy_values)

for i in range(len(final_cluster12_xy_values[0])):
    a=final_cluster12_xy_values[0][i][0]
    b=final_cluster12_xy_values[0][i][1]
    img[a][b]=center_array[0][11]

final_cluster13_xy_values=[cluster13_xy_values]
final_cluster13_xy_values=np.array(final_cluster13_xy_values)

for i in range(len(final_cluster13_xy_values[0])):
    a=final_cluster13_xy_values[0][i][0]
    b=final_cluster13_xy_values[0][i][1]
    img[a][b]=center_array[0][12]

final_cluster14_xy_values=[cluster14_xy_values]
final_cluster14_xy_values=np.array(final_cluster14_xy_values)

for i in range(len(final_cluster14_xy_values[0])):
    a=final_cluster14_xy_values[0][i][0]
    b=final_cluster14_xy_values[0][i][1]
    img[a][b]=center_array[0][13]

final_cluster15_xy_values=[cluster15_xy_values]
final_cluster15_xy_values=np.array(final_cluster15_xy_values)

for i in range(len(final_cluster15_xy_values[0])):
    a=final_cluster15_xy_values[0][i][0]
    b=final_cluster15_xy_values[0][i][1]
    img[a][b]=center_array[0][14]
    
final_cluster16_xy_values=[cluster16_xy_values]
final_cluster16_xy_values=np.array(final_cluster16_xy_values)

for i in range(len(final_cluster16_xy_values[0])):
    a=final_cluster16_xy_values[0][i][0]
    b=final_cluster16_xy_values[0][i][1]
    img[a][b]=center_array[0][15]

final_cluster17_xy_values=[cluster17_xy_values]
final_cluster17_xy_values=np.array(final_cluster17_xy_values)

for i in range(len(final_cluster17_xy_values[0])):
    a=final_cluster17_xy_values[0][i][0]
    b=final_cluster17_xy_values[0][i][1]
    img[a][b]=center_array[0][16]
    
final_cluster18_xy_values=[cluster18_xy_values]
final_cluster18_xy_values=np.array(final_cluster18_xy_values)

for i in range(len(final_cluster18_xy_values[0])):
    a=final_cluster18_xy_values[0][i][0]
    b=final_cluster18_xy_values[0][i][1]
    img[a][b]=center_array[0][17]
final_cluster19_xy_values=[cluster19_xy_values]
final_cluster19_xy_values=np.array(final_cluster19_xy_values)

for i in range(len(final_cluster19_xy_values[0])):
    a=final_cluster19_xy_values[0][i][0]
    b=final_cluster19_xy_values[0][i][1]
    img[a][b]=center_array[0][18]
    
final_cluster20_xy_values=[cluster20_xy_values]
final_cluster20_xy_values=np.array(final_cluster20_xy_values)

for i in range(len(final_cluster20_xy_values[0])):
    a=final_cluster20_xy_values[0][i][0]
    b=final_cluster20_xy_values[0][i][1]
    img[a][b]=center_array[0][19]

cv2.imwrite("task3_part4_k20.jpg",img1)



    
    



    

            
            
            
            

