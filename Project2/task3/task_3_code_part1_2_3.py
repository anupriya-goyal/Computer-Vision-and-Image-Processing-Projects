
# coding: utf-8

# In[4]:


UBIT = 'anupriya'; 
import numpy as np; 
np.random.seed(sum([ord(c) for c in UBIT]))

import matplotlib.pyplot as plt
import math

data = np.array([[5.9,3.2],[4.6,2.9],[6.2,2.8],[4.7,3.2],[5.5,4.2],[5.0,3.0],[4.9,3.1],[ 6.7,3.1],[ 5.1,3.8],[ 6.0,3.0]])
centroids = np.array([[6.2,3.2],[6.6,3.7],[6.5,3.0]])

m=0
n=0
j=0
count = 0
distance = []
cluster1 =[]
cluster2 =[]
cluster3= []
classification_vector1=[]
classification_vector2=[]
count=0
k=0
p=0
while count<=9:
    
    
    for i in range(3):
        
       
        distance.append(math.sqrt(((data[m][n]-centroids[i][j])**2)+((data[m][n+1]-centroids[i][j+1])**2)))
       
    
    a=min(distance[k],distance[k+1],distance[k+2])
    
    for p in range(k,k+3):
        if a==distance[p]:
            index= p
            
        
    if index == k:
        
        cluster1.append(data[m])
        classification_vector1.append(data[m])
        classification_vector1.append("red (cluster1)")
        
    if index==k+1:
        
        cluster2.append(data[m]) 
        classification_vector1.append(data[m])
        classification_vector1.append("green (cluster2)")
    if index==k+2:
        
        cluster3.append(data[m])
        classification_vector1.append(data[m])
        classification_vector1.append("blue (cluster3)")    
    
    
    m=m+1
    count=count+1
    k=k+3    
classification_vector1=np.array(classification_vector1) 
print("classification vector with respect to given means initially(u1,u2,u3):")
print(classification_vector1)
plt.scatter(centroids[0][0],centroids[0][1],marker='o',color='red');
plt.text(centroids[0][0],centroids[0][1],'('+str(centroids[0][0])+','+str(centroids[0][1])+')')
    
plt.scatter(centroids[1][0],centroids[1][1],marker='o',color='green');
plt.text(centroids[1][0],centroids[1][1],'('+str(centroids[1][0])+','+str(centroids[1][1])+')')
 
task3_iter1_a=plt.scatter(centroids[2][0],centroids[2][1],marker='o',color='blue');
plt.text(centroids[2][0],centroids[2][1],'('+str(centroids[2][0])+','+str(centroids[2][1])+')')
 

y=0
for x in range(len(cluster1)):
    
    plt.scatter(cluster1[x][y], cluster1[x][y+1], marker='^',color='red');
    plt.text(cluster1[x][y],cluster1[x][y+1],'('+str(cluster1[x][y])+','+str(cluster1[x][y+1])+')')
    

for x in range(len(cluster2)):
    plt.scatter(cluster2[x][y], cluster2[x][y+1], marker='^',color='green');
    plt.text(cluster2[x][y],cluster2[x][y+1],'('+str(cluster2[x][y])+','+str(cluster2[x][y+1])+')')
    

for x in range(len(cluster3)):
    task3_iter1_a=plt.scatter(cluster3[x][y], cluster3[x][y+1], marker='^',color='blue');
    plt.text(cluster3[x][y],cluster3[x][y+1],'('+str(cluster3[x][y])+','+str(cluster3[x][y+1])+')')



plt.savefig('task3_iter1_a.jpg')
#clears the previous plot
plt.clf() 
#new centers for clusters
new_cluster1 =[]
new_cluster_a=[]
j=0
sum_x=0
for i in range(len(cluster1)):
        
        sum_x=cluster1[i][j]+sum_x
        

new_cluster_a.append((sum_x+centroids[0][0])/(len(cluster1)+1))
new_cluster1.append((sum_x)/(len(cluster1)))

j=0
sum_y=0
for i in range(len(cluster1)):
        
        sum_y=cluster1[i][j+1]+sum_y
        
a=((sum_y)/(len(cluster1)))
new_cluster_a.append(((sum_y+centroids[0][1])/(len(cluster1)+1)))
new_cluster1.append(a)

new_cluster2 =[]
new_cluster_b=[]
j=0
sum_x=0
for i in range(len(cluster2)):
        
        sum_x=cluster2[i][j]+sum_x
        

new_cluster2.append((sum_x)/(len(cluster2)))
new_cluster_b.append((sum_x+centroids[1][0])/(len(cluster2)+1))


j=0
sum_y=0
for i in range(len(cluster2)):
        
        sum_y=cluster2[i][j+1]+sum_y
        
a=((sum_y)/(len(cluster2)))
new_cluster2.append(a)
new_cluster_b.append((sum_y+centroids[1][1])/(len(cluster2)+1))

new_cluster3 =[]
new_cluster_c=[]
j=0
sum_x=0
for i in range(len(cluster3)):
        
        sum_x=cluster3[i][j]+sum_x
        

new_cluster3.append((sum_x)/(len(cluster3)))
new_cluster_c.append((sum_x+centroids[2][0])/(len(cluster3)+1))


j=0
sum_y=0
for i in range(len(cluster3)):
       
        sum_y=cluster3[i][j+1]+sum_y
        
a=((sum_y)/(len(cluster3)))
new_cluster3.append(a)
new_cluster_c.append((sum_y+centroids[2][1])/(len(cluster3)+1))

plt.scatter(new_cluster_a[0], new_cluster_a[1], marker='o',color='red');
plt.text(new_cluster_a[0], new_cluster_a[1],'('+str(new_cluster_a[0])+','+str(new_cluster_a[1])+')')
plt.scatter(new_cluster_b[0], new_cluster_b[1], marker='o',color='green');
plt.text(new_cluster_b[0], new_cluster_b[1],'('+str(new_cluster_b[0])+','+str(new_cluster_b[1])+')')
plt.scatter(new_cluster_c[0], new_cluster_c[1], marker='o',color='blue');
plt.text(new_cluster_c[0], new_cluster_c[1],'('+str(new_cluster_c[0])+','+str(new_cluster_c[1])+')')
centroids_up =[]  
centroids_up = np.array([[new_cluster_a[0],new_cluster_a[1]],[new_cluster_b[0],new_cluster_b[1]],[new_cluster_c[0],new_cluster_c[1]]])
plt.savefig('task3_iter1_b.jpg')
plt.clf()

#2nd iteration
centroids = np.array([[new_cluster1[0],new_cluster1[1]],[new_cluster2[0],new_cluster2[1]],[new_cluster3[0],new_cluster3[1]]])
print(" ")
print("Updated mean values u1,u2,u3 first iteration:")
print(centroids_up)

m=0
n=0
j=0
count = 0
distance = []
cluster1 =[]
cluster2 =[]
cluster3= []
count=0
k=0
p=0
while count<=9:
    
    for i in range(3):
        
       
        distance.append(math.sqrt(((data[m][n]-centroids[i][j])**2)+((data[m][n+1]-centroids[i][j+1])**2)))
       
    
    a=min(distance[k],distance[k+1],distance[k+2])
    
    for p in range(k,k+3):
        if a==distance[p]:
            index= p
            
        
        
    if index == k:
        
        cluster1.append(data[m])
        classification_vector2.append(data[m])
        classification_vector2.append("red (cluster1)")
    if index==k+1:
        
        cluster2.append(data[m])
        classification_vector2.append(data[m])
        classification_vector2.append("green (cluster2)")
    if index==k+2:
        
        cluster3.append(data[m])
        classification_vector2.append(data[m])
        classification_vector2.append("blue (cluster3)")   
    
    
    
    m=m+1
    count=count+1
    k=k+3
#new centers for clusters


new_cluster1 =[]
j=0
sum_x=0
for i in range(len(cluster1)):
        #print(cluster1[i][j])
        sum_x=cluster1[i][j]+sum_x
        #print(sum_x)

new_cluster1.append((sum_x)/(len(cluster1)))


j=0
sum_y=0
for i in range(len(cluster1)):
        
        sum_y=cluster1[i][j+1]+sum_y
        
a=((sum_y)/(len(cluster1)))
new_cluster1.append(a)


new_cluster2 =[]
j=0
sum_x=0
for i in range(len(cluster2)):
        #print(cluster2[i][j])
        sum_x=cluster2[i][j]+sum_x
        #print(sum_x)

new_cluster2.append((sum_x)/(len(cluster2)))


j=0
sum_y=0
for i in range(len(cluster2)):
        #print(cluster2[i][j+1])
        sum_y=cluster2[i][j+1]+sum_y
        #print(sum_y)
a=((sum_y)/(len(cluster2)))
new_cluster2.append(a)

new_cluster3 =[]
j=0
sum_x=0
for i in range(len(cluster3)):
        #print(cluster1[i][j])
        sum_x=cluster3[i][j]+sum_x
        #print(sum_x)

new_cluster3.append((sum_x)/(len(cluster3)))


j=0
sum_y=0
for i in range(len(cluster3)):
        #print(cluster2[i][j+1])
        sum_y=cluster3[i][j+1]+sum_y
        #print(sum_y)
a=((sum_y)/(len(cluster3)))
new_cluster3.append(a)

centroids = np.array([[new_cluster1[0],new_cluster1[1]],[new_cluster2[0],new_cluster2[1]],[new_cluster3[0],new_cluster3[1]]])
print(" ")
print("updated mean values u1,u2,u3: Second Iteration")
print(centroids)

#classification_vector=np.array(classification_vector)   
plt.scatter(centroids[0][0],centroids[0][1],marker='o',color='red');
plt.text(centroids[0][0],centroids[0][1],'('+str(centroids[0][0])+','+str(centroids[0][1])+')')
    
plt.scatter(centroids[1][0],centroids[1][1],marker='o',color='green');
plt.text(centroids[1][0],centroids[1][1],'('+str(centroids[1][0])+','+str(centroids[1][1])+')')
 
task3_iter1_a=plt.scatter(centroids[2][0],centroids[2][1],marker='o',color='blue');
plt.text(centroids[2][0],centroids[2][1],'('+str(centroids[2][0])+','+str(centroids[2][1])+')')


plt.savefig('task3_iter2_b.jpg')
#plt.clf()


y=0
for x in range(len(cluster1)):
    
    plt.scatter(cluster1[x][y], cluster1[x][y+1], marker='^',color='red');
    plt.text(cluster1[x][y],cluster1[x][y+1],'('+str(cluster1[x][y])+','+str(cluster1[x][y+1])+')')
    

for x in range(len(cluster2)):
    plt.scatter(cluster2[x][y], cluster2[x][y+1], marker='^',color='green');
    plt.text(cluster2[x][y],cluster2[x][y+1],'('+str(cluster2[x][y])+','+str(cluster2[x][y+1])+')')
    

for x in range(len(cluster3)):
    task3_iter1_a=plt.scatter(cluster3[x][y], cluster3[x][y+1], marker='^',color='blue');
    plt.text(cluster3[x][y],cluster3[x][y+1],'('+str(cluster3[x][y])+','+str(cluster3[x][y+1])+')')

plt.savefig('task3_iter2_a.jpg')
    

classification_vector2=np.array(classification_vector2) 
print("classification vector: Second iteration:")
print(classification_vector2)

