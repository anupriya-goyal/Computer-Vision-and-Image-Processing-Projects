
# coding: utf-8

# In[ ]:


#Task3 Bonus task
import cv2
import numpy as np

read_img = cv2.imread('hough.jpg',1)

gaussain_blur = cv2.GaussianBlur(read_img,(3,3),0)


detect_edge = cv2.Canny(gaussain_blur,75,150)



r = 100
h,w =detect_edge.shape


container_st = np.zeros(((h,w,r)))

circle_3dim = np.zeros((30,30,r))
circle_3dim[:,:,:]=1
resultant = read_img.copy()


def hough_trans_circle(x0,y0,r_d):
    cord_x = r_d
    cord_y=0
    cond_fact = 1-cord_x
    
    while(cord_y<cord_x ):
        if(cord_x + x0<h and cord_y + y0<w):
            container_st [ cord_x + x0,cord_y + y0,r_d]+=1; 
        if(cord_y  + x0<h and cord_x + y0<w):
            container_st [ cord_y  + x0,cord_x + y0,r_d]+=1; 
        if(-cord_x + x0<h and cord_y + y0<w):
            container_st [-cord_x + x0,cord_y  + y0,r_d]+=1; 
        if(-cord_y  + x0<h and cord_x + y0<w):
            container_st [-cord_y  + x0,cord_x + y0,r_d]+=1; 
        if(-cord_x + x0<h and -cord_y  + y0<w):
            container_st [-x + x0,-cord_y  + y0,r_d]+=1; 
        if(-cord_y  + x0<h and -cord_x + y0<w):
            container_st [-cord_y  + x0,-x + y0,r_d]+=1; 
        if(cord_x + x0<h and -cord_y  + y0<w):
            container_st [ cord_x + x0,-cord_y  + y0,r_d]+=1; 
        if(cord_y  + x0<h and -cord_x + y0<w):
            container_st [ cord_y  + x0,-cord_x + y0,r_d]+=1;
        cord_y+=1
        if(cond_fact<=0):
            cond_fact += 2 * cord_y + 1
        else:
            cord_x=cord_x-1;
            cond_fact+= 2 * (cord_y - cord_x) + 1
    
    
found_edge = np.where(detect_edge==255)
for i in range(0,len(found_edge[0])):
    x=found_edge[0][i]
    y=found_edge[1][i]
    for radius in range(20,55):
        hough_trans_circle(x,y,radius)
            

iterator=0
second_iter=0
while(iterator<h-30):
    while(second_iter<w-30):
        circle_3dim =container_st[iterator:iterator+30,second_iter:second_iter+30,:]*circle_3dim 
        maxima = np.where(circle_3dim ==circle_3dim.max())
        a = maxima[0]       
        b = maxima[1]
        c = maxima[2]
        b=b+second_iter
        a=a+iterator
        if(circle_3dim.max()>90):
            cv2.circle(resultant,(b,a),c,(0,255,0),2)
        second_iter=second_iter+30
        circle_3dim[:,:,:]=1
    second_iter=0
    iterator=iterator+30
                


cv2.imwrite("coin.jpg",resultant)
cv2.waitKey(0)
cv2.destroyAllWindows()

