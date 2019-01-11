
# coding: utf-8

# In[ ]:


# References for task 2
#1.https://stackoverflow.com/questions/8204645/implementing-gaussian-blur-how-to-calculate-convolution-matrix-kernel 
# this is used for gaussain kernel implementation
#2.http://aishack.in/tutorials/sift-scale-invariant-feature-transform-introduction/
#3. aishack.in/tutorials/sift-scale-invariant-feature-transform-keypoints/


# In[15]:


# Task2 for KeyPoint Detection in an image.
import math
import cv2 
import numpy as np


# In[16]:


#Read image from particular folder
org_img = cv2.imread("path\\task2.jpg",0)


# In[17]:


#copy of image is created to add padding to it
copy_org_img=org_img.copy()
copy_org_img[0,:] = copy_org_img[:,0] = copy_org_img[:,-3] =  copy_org_img[-3,:] = 0
rows=org_img.shape[0]
column=org_img.shape[1]


# In[18]:


# these denotes dog for 1st octave. Used it to denote rest of octaves in each convolution
d11=copy_org_img.copy()
d12=copy_org_img.copy()
d13=copy_org_img.copy()
d14=copy_org_img.copy()


# In[19]:


#creating matrix to add new values after convolution
conv_res1=copy_org_img.copy()
conv_res2=copy_org_img.copy()
conv_res3=copy_org_img.copy()
conv_res4=copy_org_img.copy()
conv_res5=copy_org_img.copy()


# In[20]:


#perfomed gaussian kernel opeartion for all octaves 
gauss1=np.zeros((7,7));
gauss2=np.zeros((7,7));
gauss3=np.zeros((7,7));
gauss4=np.zeros((7,7));
gauss5=np.zeros((7,7));
gauss6=np.zeros((7,7));
gauss7=np.zeros((7,7));
gauss8=np.zeros((7,7));
gauss9=np.zeros((7,7));
gauss10=np.zeros((7,7));
gauss11=np.zeros((7,7));
gauss12=np.zeros((7,7));
gauss13=np.zeros((7,7));
gauss14=np.zeros((7,7));
gauss15=np.zeros((7,7));
gauss16=np.zeros((7,7));
gauss17=np.zeros((7,7));
gauss18=np.zeros((7,7));
gauss19=np.zeros((7,7));
gauss20=np.zeros((7,7));


# In[21]:


#used add_ variable to normalise the gaussain kernel
add_1=0.0
add_2=0.0
add_3=0.0
add_4=0.0
add_5=0.0
add_6=0.0
add_7=0.0
add_8=0.0
add_9=0.0
add_10=0.0
add_11=0.0
add_12=0.0
add_13=0.0
add_14=0.0
add_15=0.0
add_16=0.0
add_17=0.0
add_18=0.0
add_19=0.0
add_20=0.0
R1=0
R2=0
R3=0
R4=0
R5=0
#sigma is the list that conatins all octaves sigma values
sigma =[(float(1/math.sqrt(2))),1,math.sqrt(2),2,(2*math.sqrt(2)),(math.sqrt(2)),2,2*math.sqrt(2),4,(4*math.sqrt(2)),(2*math.sqrt(2)),4,4*math.sqrt(2),8,(8*math.sqrt(2)),(2*math.sqrt(2)),4,4*math.sqrt(2),8,(8*math.sqrt(2))]

a=-3
b=4

for x in range(a,b):
    for y in range(a,b):
        gauss1[x][y] =( math.exp( -(0.5 * float((pow((x)/sigma[0], 2.0) + pow((y)/sigma[0],2.0) )))))/  (2 * math.pi * sigma[0] * sigma[0])
        gauss2[x][y] =( math.exp( -(0.5 * float((pow((x)/sigma[1], 2.0) + pow((y)/sigma[1],2.0) )))))/  (2 * math.pi * sigma[1] * sigma[1])
        gauss3[x][y] =( math.exp( -(0.5 * float((pow((x)/sigma[2], 2.0) + pow((y)/sigma[2],2.0) )))))/  (2 * math.pi * sigma[2] * sigma[2])
        gauss4[x][y] =( math.exp( -(0.5 * float((pow((x)/sigma[3], 2.0) + pow((y)/sigma[3],2.0) )))))/  (2 * math.pi * sigma[3] * sigma[3])
        gauss5[x][y] =( math.exp( -(0.5 * float((pow((x)/sigma[4], 2.0) + pow((y)/sigma[4],2.0) )))))/  (2 * math.pi * sigma[4] * sigma[4])
        gauss6[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[5], 2.0) + pow((y)/sigma[5],2.0) ))))/  (2 * math.pi * sigma[5] * sigma[5])
        gauss7[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[6], 2.0) + pow((y)/sigma[6],2.0) ))))/  (2 * math.pi * sigma[6] * sigma[6])
        gauss8[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[7], 2.0) + pow((y)/sigma[7],2.0) ))))/  (2 * math.pi * sigma[7] * sigma[7])
        gauss9[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[8], 2.0) + pow((y)/sigma[8],2.0) ))))/  (2 * math.pi * sigma[8] * sigma[8])
        gauss10[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[9], 2.0) + pow((y)/sigma[9],2.0) ))))/  (2 * math.pi * sigma[9] * sigma[9])
        gauss11[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[10], 2.0) + pow((y)/sigma[10],2.0) ))))/  (2 * math.pi * sigma[10] * sigma[10])
        gauss12[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[11], 2.0) + pow((y)/sigma[11],2.0) ))))/  (2 * math.pi * sigma[11] * sigma[11])
        gauss13[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[12], 2.0) + pow((y)/sigma[12],2.0) ))))/  (2 * math.pi * sigma[12] * sigma[12])
        gauss14[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[13], 2.0) + pow((y)/sigma[13],2.0) ))))/  (2 * math.pi * sigma[13] * sigma[13])
        gauss15[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[14], 2.0) + pow((y)/sigma[14],2.0) ))))/  (2 * math.pi * sigma[14] * sigma[14])
        gauss16[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[15], 2.0) + pow((y)/sigma[15],2.0) ))))/  (2 * math.pi * sigma[15] * sigma[15])
        gauss17[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[16], 2.0) + pow((y)/sigma[16],2.0) ))))/  (2 * math.pi * sigma[16] * sigma[16])
        gauss18[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[17], 2.0) + pow((y)/sigma[17],2.0) ))))/  (2 * math.pi * sigma[17] * sigma[17])
        gauss19[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[18], 2.0) + pow((y)/sigma[18],2.0) ))))/  (2 * math.pi * sigma[18] * sigma[18])
        gauss20[x][y] =( math.exp( -0.5 * float((pow((x)/sigma[19], 2.0) + pow((y)/sigma[19],2.0) ))))/  (2 * math.pi * sigma[19] * sigma[19])
        add_1 += gauss1[x][y]
        add_2 += gauss2[x][y]
        add_3 += gauss3[x][y]
        add_4 += gauss4[x][y]
        add_5 += gauss5[x][y]
        add_6 += gauss6[x][y]
        add_7 += gauss7[x][y]
        add_8 += gauss8[x][y]
        add_9 += gauss9[x][y]
        add_10 += gauss10[x][y]
        add_11 += gauss11[x][y]
        add_12 += gauss12[x][y]
        add_13 += gauss13[x][y]
        add_14 += gauss14[x][y]
        add_15 += gauss15[x][y]
        add_16 += gauss16[x][y]
        add_17 += gauss17[x][y]
        add_18 += gauss18[x][y]
        add_19 += gauss19[x][y]
        add_20 += gauss20[x][y]
       



    
    
for x in range(0,7):
    for y in range(0,7): 
        gauss1[x][y]=float(gauss1[x][y]/add_1)
        gauss2[x][y]=float(gauss2[x][y]/add_2)
        gauss3[x][y]=float(gauss3[x][y]/add_3)
        gauss4[x][y]=float(gauss4[x][y]/add_4)
        gauss5[x][y]=float(gauss5[x][y]/add_5)
        gauss6[x][y]=float(gauss6[x][y]/add_6)
        gauss7[x][y]=float(gauss7[x][y]/add_7)
        gauss8[x][y]=float(gauss8[x][y]/add_8)
        gauss9[x][y]=float(gauss9[x][y]/add_9)
        gauss10[x][y]=float(gauss10[x][y]/add_10)
        gauss11[x][y]=float(gauss11[x][y]/add_11)
        gauss12[x][y]=float(gauss12[x][y]/add_12)
        gauss13[x][y]=float(gauss13[x][y]/add_13)
        gauss14[x][y]=float(gauss14[x][y]/add_14)
        gauss15[x][y]=float(gauss15[x][y]/add_15)
        gauss16[x][y]=float(gauss16[x][y]/add_16)
        gauss17[x][y]=float(gauss17[x][y]/add_17)
        gauss18[x][y]=float(gauss18[x][y]/add_18)
        gauss19[x][y]=float(gauss19[x][y]/add_19)
        gauss20[x][y]=float(gauss20[x][y]/add_20)
    
   #kernel is normalised 
    
    


# In[22]:


# Finding Dog's for all octaves in the below manner by performing convolution
for x in range(0, rows):  
    for y in range (0,column):
        for i in range(1,7):
            for j in range(1,7):
                R1+=gauss1[i-1][j-1]*org_img[x-(i-1)][y-(j-1)]
                R2+=gauss2[i-1][j-1]*org_img[x-(i-1)][y-(j-1)]
                R3+=gauss3[i-1][j-1]*org_img[x-(i-1)][y-(j-1)]
                R4+=gauss4[i-1][j-1]*org_img[x-(i-1)][y-(j-1)]
                R5+=gauss5[i-1][j-1]*org_img[x-(i-1)][y-(j-1)]
        conv_res1[x][y]=R1
        conv_res2[x][y]=R2
        conv_res3[x][y]=R3
        conv_res4[x][y]=R4
        conv_res5[x][y]=R5
        R1=0
        R2=0
        R3=0
        R4=0
        R5=0
        
for x in range(0, rows):  
    for y in range (0,column):
        d11[x][y]= conv_res2[x][y]- conv_res1[x][y]
        d12[x][y]= conv_res3[x][y]- conv_res2[x][y]
        d13[x][y]= conv_res4[x][y]- conv_res3[x][y]
        d14[x][y]= conv_res5[x][y]- conv_res4[x][y]
       



 

 
#cv2.imshow('dog1',d11)
#cv2.imshow('dog2',d12)
#cv2.imshow('dog3',d13)
#cv2.imshow('dog4',d14)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# In[23]:


hi,wt=conv_res1.shape
resize1_img=cv2.resize(conv_res1, (wt//2, hi//2)) 
height=resize1_img.shape[0]
width=resize1_img.shape[1]      
conv2_res1=resize1_img.copy()
conv2_res2=resize1_img.copy()
conv2_res3=resize1_img.copy()
conv2_res4=resize1_img.copy()
conv2_res5=resize1_img.copy()
d21=resize1_img.copy()
d22=resize1_img.copy()
d23=resize1_img.copy()
d24=resize1_img.copy()

for x in range(0, height):  
    for y in range (0,width):
        for i in range(1,7):
            for j in range(1,7):
                R1+=gauss6[i-1][j-1]*resize1_img[x-(i-1)][y-(j-1)]
                R2+=gauss7[i-1][j-1]*resize1_img[x-(i-1)][y-(j-1)]
                R3+=gauss8[i-1][j-1]*resize1_img[x-(i-1)][y-(j-1)]
                R4+=gauss9[i-1][j-1]*resize1_img[x-(i-1)][y-(j-1)]
                R5+=gauss10[i-1][j-1]*resize1_img[x-(i-1)][y-(j-1)]
        conv2_res1[x][y]=R1
        conv2_res2[x][y]=R2
        conv2_res3[x][y]=R3
        conv2_res4[x][y]=R4
        conv2_res5[x][y]=R5
        R1=0
        R2=0
        R3=0
        R4=0
        R5=0
        
for x in range(0, height):  
    for y in range (0,width):
        d21[x][y]= conv2_res2[x][y]- conv2_res1[x][y]
        d22[x][y]= conv2_res3[x][y]- conv2_res2[x][y]
        d23[x][y]= conv2_res4[x][y]- conv2_res3[x][y]
        d24[x][y]= conv2_res5[x][y]- conv2_res4[x][y]
        
#cv2.imshow('dog5',d21)
#cv2.imshow('dog6',d22)
#cv2.imshow('dog7',d23)
#cv2.imshow('dog8',d24)
#cv2.imshow('resize',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()   


# In[24]:


h=resize1_img.shape[0]
w=resize1_img.shape[1]
resize2_img=cv2.resize(resize1_img,( (w//2),(h//2)) )
height=resize2_img.shape[0]
width=resize2_img.shape[1]      
#img1=img_01.copy()
conv3_res1=resize2_img.copy()
conv3_res2=resize2_img.copy()
conv3_res3=resize2_img.copy()
conv3_res4=resize2_img.copy()
conv3_res5=resize2_img.copy()
R1=0
R2=0
R3=0
R4=0
R5=0
d31=resize2_img.copy()
d32=resize2_img.copy()
d34=resize2_img.copy()
d35=resize2_img.copy()
for x in range(0, height):  
    for y in range (0,width):
        for i in range(1,7):
            for j in range(1,7):
                R1+=gauss11[i-1][j-1]*resize2_img[x-(i-1)][y-(j-1)]
                R2+=gauss12[i-1][j-1]*resize2_img[x-(i-1)][y-(j-1)]
                R3+=gauss13[i-1][j-1]*resize2_img[x-(i-1)][y-(j-1)]
                R4+=gauss14[i-1][j-1]*resize2_img[x-(i-1)][y-(j-1)]
                R5+=gauss15[i-1][j-1]*resize2_img[x-(i-1)][y-(j-1)]
        conv3_res1[x][y]=R1
        conv3_res2[x][y]=R2
        conv3_res3[x][y]=R3
        conv3_res4[x][y]=R4
        conv3_res5[x][y]=R5
        R1=0
        R2=0
        R3=0
        R4=0
        R5=0
for x in range(0, height):  
    for y in range (0,width):
        d31[x][y]=conv3_res2[x][y]-conv3_res1[x][y]
        d32[x][y]=conv3_res3[x][y]-conv3_res2[x][y]
        d34[x][y]=conv3_res4[x][y]-conv3_res3[x][y]
        d35[x][y]=conv3_res5[x][y]-conv3_res4[x][y]
 

 
#cv2.imshow('dog9',d31)
#cv2.imshow('dog10',d32)
#cv2.imshow('dog11',d34)
#cv2.imshow('dog12',d35)
#cv2.imshow('resize',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows() 


# In[ ]:


h,w=resize2_img.shape

resize3_img=cv2.resize(resize2_img, (w//2, h//2)) 
height=resize3_img.shape[0]
width=resize3_img.shape[1] 

conv4_res1=resize3_img.copy()
conv4_res2=resize3_img.copy()
conv4_res3=resize3_img.copy()
conv4_res4=resize3_img.copy()
conv4_res5=resize3_img.copy()
d41=resize3_img.copy()
d42=resize3_img.copy()
d43=resize3_img.copy()
d45=resize3_img.copy()


R1=0
R2=0
R3=0
R4=0
R5=0

for x in range(0, height):  
    for y in range (0,width):
        for i in range(1,7):
            for j in range(1,7):
                R1+=gauss16[i-1][j-1]*resize3_img[x-(i-1)][y-(j-1)]
                R2+=gauss17[i-1][j-1]*resize3_img[x-(i-1)][y-(j-1)]
                R3+=gauss18[i-1][j-1]*resize3_img[x-(i-1)][y-(j-1)]
                R4+=gauss19[i-1][j-1]*resize3_img[x-(i-1)][y-(j-1)]
                R5+=gauss20[i-1][j-1]*resize3_img[x-(i-1)][y-(j-1)]
        conv4_res1[x][y]=R1
        conv4_res2[x][y]=R2
        conv4_res3[x][y]=R3
        conv4_res4[x][y]=R4
        conv4_res5[x][y]=R5
        R1=0
        R2=0
        R3=0
        R4=0
        R5=0
for x in range(0, height):  
    for y in range (0,width):
        d41[x][y]= conv4_res2[x][y]- conv4_res1[x][y]
        d42[x][y]= conv4_res3[x][y]- conv4_res2[x][y]
        d43[x][y]= conv4_res4[x][y]- conv4_res3[x][y]
        d45[x][y]= conv4_res5[x][y]- conv4_res4[x][y]
       



    
#cv2.imshow('dog13',d41)
#cv2.imshow('dog14',d42)
#cv2.imshow('dog15',d43)
#cv2.imshow('dog16',d45)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
# a key_point function gets the key points from the dog's and mark them in original image
def key_point(array_d_1,array_d_2,array_d_3):
 for i in range(0,h-3,3):
     for j in range(0,w-3,3):
          
            value_max= array_d_2[i+3//2][j+3//2]
            loc1=0
            loc2=0
            
            if(value_max<np.max(array_d_1)):
                value_max=np.max(array_d_1)
                for k in range(1,4):
                  for l in range(1,4):
                      if(value_max==array_d_1[i+k][j+l]):
                          loc1=i+k
                          loc2=j+l
            if(value_max<np.max(array_d_2)):
                value_max=np.max(array_d_1)
                for k in range(1,4):
                  for l in range(1,4):
                      if(value_max==array_d_1[i+k][j+l]):
                          loc1=i+k
                          loc2=j+l
            if(value_max<np.max(array_d_3)):
                maximum=np.max(array_d_1)
                for k in range(1,4):
                  for l in range(1,4):
                      if(value_max==array_d_1[i+k][j+l]):
                          loc1=i+k
                          loc2=j+l
            
            org_img[loc1][loc2]=255
            
h,w=copy_org_img.shape
key_point(d11,d12,d13)
key_point(d12,d13,d14)
h,w=resize1_img.shape
key_point(d21,d22,d23)
key_point(d22,d23,d24)
h,w=resize2_img.shape
key_point(d31,d32,d34)
key_point(d32,d34,d35)
h,w=resize3_img.shape
key_point(d41,d42,d43)
key_point(d42,d43,d45)
cv2.imshow('Img',org_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

