#LIBRARY =============================================================================
import pandas as pd
import math
import Validations_FINAL as validations



#DATASET
dataset=pd.read_csv("dataset/norm.csv")
original=dataset.iloc[0:156,1:5].values   #case1 
original2=dataset.iloc[0:156, [1,2]].values #case2
original3=dataset.iloc[0:156, [5,6]].values #case3 
belong = dataset.iloc[0:156,9].values 


##################################-----##################################
################################ case1 ##################################
################################-----####################################
#initialising centroids for the first time
c1 =[0.86,108,0.9,14]
c2 =[1.27,136,0.79,10]

n=0
while(n<100):
   #membership value=case1==============================================================================
   r=0
   c=0
   row,col=(156,2)
   u=[[0 for p in range(col)] for q in range(row)]
   for row in original:
       aa=math.sqrt(((row[0]- c1[0])**2)+((row[1]- c1[1])**2)+((row[2]- c1[2])**2)+((row[3]- c1[3])**2))
       bb=math.sqrt(((row[0]- c2[0])**2)+((row[1]- c2[1])**2)+((row[2]- c2[2])**2)+((row[3]- c2[3])**2))
       u1=(aa)/(bb)
       cc=math.sqrt(((row[0]- c2[0])**2)+((row[1]- c2[1])**2)+((row[2]- c2[2])**2)+((row[3]- c2[3])**2))
       dd=math.sqrt(((row[0]- c1[0])**2)+((row[1]- c1[1])**2)+((row[2]- c1[2])**2)+((row[3]- c1[3])**2))
       u2=(cc)/(dd)
       u[r][0]=1/(1+((u1)**2))
       u[r][1]=1/(1+((u2)**2))    
       r=r+1
   #centroid c1 =case1===================================================================================
   sum1=0
   sum2=0 
   sumden=0  
   r=0
   for x in range(156):
       sumden=sumden+((u[x][0])**2)
   for row in original:
       sum1=sum1+row[0]*((u[r][0])**2)
       sum2=sum2+row[1]*((u[r][0])**2)
       r=r+1
   c1[0]=sum1/sumden
   c1[1]=sum2/sumden

   #centroid c2  =case1==================================================================================
   sum1=0
   sum2=0 
   r=0 
   sumden=0  
   r=0
   for x in range(156):
       sumden=sumden+((u[x][1])**2)
   for row in original:
       sum1=sum1+row[0]*((u[r][1])**2)
       sum2=sum2+row[1]*((u[r][1])**2)
       r=r+1
   c2[0]=sum1/sumden
   c2[1]=sum2/sumden
   
   n=n+1

centroids=[c1,c2]
a=0
cluster0=0
cluster1=0

#true positive
tp=0
w=0
c=[0 for q in range(156)]
for row in u:
    w=w+1
    if(row[0]>row[1]):
        c[a]=0
        cluster0=cluster0+1 
        if(belong[a]==c[a]):
            tp=tp+1
    else:
        c[a]=1 
        cluster1=cluster1+1
        if(belong[a]==c[a]):
            tp=tp+1
   #print(c[a])
    a=a+1
#making clusters
c0array=[[0 for p in range(2)] for q in range(cluster0)]
c1array=[[0 for p in range(2)] for q in range(cluster1)]
a=i=j=0
for row in original2: 
    if(c[a]== 0):
        c0array[i][0]=row[0]
        c0array[i][1]=row[1]
        i=i+1
    if(c[a]== 1):
        c1array[j][0]=row[0]
        c1array[j][1]=row[1]
        j=j+1
    a=a+1
aaaa=pd.DataFrame(c0array)     
cccc=pd.DataFrame(c1array)     

   
#validity index
fcpi_1=validations.fCPI(u,belong)
fintra_1=validations.Intra(original,c,cluster0,cluster1)
finter_1=validations.Inter(original,c,cluster0,cluster1)
fsi_1 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
fmse_1=validations.MSE(c,belong)
fdi_1= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)

   


##################################-----##################################
################################ case2 ##################################
################################-----####################################

c1=[0.9,140] #intact
c2=[1101.0,117.00] #cp
n=0
while(n<100):
   #membership value=case2==============================================================================
   r=0
   c=0
   row,col=(156,2)
   u=[[0 for p in range(col)] for q in range(row)]
   for row in original2:
       aa=math.sqrt(((row[0]- c1[0])**2)+((row[1]- c1[1])**2))
       bb=math.sqrt(((row[0]- c2[0])**2)+((row[1]- c2[1])**2))
       u1=(aa)/(bb)
       cc=math.sqrt(((row[0]- c2[0])**2)+((row[1]- c2[1])**2))
       dd=math.sqrt(((row[0]- c1[0])**2)+((row[1]- c1[1])**2))
       u2=(cc)/(dd)
       u[r][0]=1/(1+((u1)**2))
       u[r][1]=1/(1+((u2)**2))    
       r=r+1
   #centroid c1 =case2===================================================================================
   sum1=0
   sum2=0 
   sumden=0  
   r=0
   for x in range(156):
       sumden=sumden+((u[x][0])**2)
   for row in original2:
       sum1=sum1+row[0]*((u[r][0])**2)
       sum2=sum2+row[1]*((u[r][0])**2)
       r=r+1
   c1[0]=sum1/sumden
   c1[1]=sum2/sumden

   #centroid c2  =case2==================================================================================
   sum1=0
   sum2=0 
   r=0 
   sumden=0  
   r=0
   for x in range(156):
       sumden=sumden+((u[x][1])**2)
   for row in original2:
       sum1=sum1+row[0]*((u[r][1])**2)
       sum2=sum2+row[1]*((u[r][1])**2)
       r=r+1
   c2[0]=sum1/sumden
   c2[1]=sum2/sumden
   
   n=n+1

#loop ends
   
a=0
cluster0=0
cluster1=0
tp=0
w=0
c=[0 for q in range(156)]
for row in u:
    w=w+1
    if(row[0]>row[1]):
        c[a]=0
        cluster0=cluster0+1 
        if(belong[a]==c[a]):
            tp=tp+1
    else:
        c[a]=1 
        cluster1=cluster1+1
        if(belong[a]==c[a]):
            tp=tp+1
   #print(c[a])
    a=a+1
#making clusters
c0array=[[0 for p in range(2)] for q in range(cluster0)]
c1array=[[0 for p in range(2)] for q in range(cluster1)]
a=i=j=0
for row in original2: 
    if(c[a]== 0):
        c0array[i][0]=row[0]
        c0array[i][1]=row[1]
        i=i+1
    if(c[a]== 1):
        c1array[j][0]=row[0]
        c1array[j][1]=row[1]
        j=j+1
    a=a+1
aaaa=pd.DataFrame(c0array)     
cccc=pd.DataFrame(c1array)     

   
#validity indexes
fcpi_2=validations.fCPI(u,belong)
fintra_2=validations.Intra(original2,c,cluster0,cluster1)
finter_2=validations.Inter(original2,c,cluster0,cluster1)
fsi_2 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
fmse_2=validations.MSE(c,belong)
fdi_2= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)


##################################-----##################################
################################ case3 ##################################
################################-----####################################
c1=[0.2372	,155.41]
c2=[0.4815	,142.99]

n=0
while(n<100):
   #membership value=case2==============================================================================
   r=0
   c=0
   row,col=(156,2)
   u=[[0 for p in range(col)] for q in range(row)]
   for row in original3:
       aa=math.sqrt(((row[0]- c1[0])**2)+((row[1]- c1[1])**2))
       bb=math.sqrt(((row[0]- c2[0])**2)+((row[1]- c2[1])**2))
       u1=(aa)/(bb)
       cc=math.sqrt(((row[0]- c2[0])**2)+((row[1]- c2[1])**2))
       dd=math.sqrt(((row[0]- c1[0])**2)+((row[1]- c1[1])**2))
       u2=(cc)/(dd)
       u[r][0]=1/(1+((u1)**2))
       u[r][1]=1/(1+((u2)**2))    
       r=r+1
   #centroid c1 =case2===================================================================================
   sum1=0
   sum2=0 
   sumden=0  
   r=0
   for x in range(156):
       sumden=sumden+((u[x][0])**2)
   for row in original3:
       sum1=sum1+row[0]*((u[r][0])**2)
       sum2=sum2+row[1]*((u[r][0])**2)
       r=r+1
   c1[0]=sum1/sumden
   c1[1]=sum2/sumden

   #centroid c2  =case2==================================================================================
   sum1=0
   sum2=0 
   r=0 
   sumden=0  
   r=0
   for x in range(156):
       sumden=sumden+((u[x][1])**2)
   for row in original3:
       sum1=sum1+row[0]*((u[r][1])**2)
       sum2=sum2+row[1]*((u[r][1])**2)
       r=r+1
   c2[0]=sum1/sumden
   c2[1]=sum2/sumden
   
   n=n+1

#loop ends
   
a=0
cluster0=0
cluster1=0
tp=0
w=0
c=[0 for q in range(156)]
for row in u:
    w=w+1
    if(row[0]>row[1]):
        c[a]=0
        cluster0=cluster0+1 
        if(belong[a]==c[a]):
            tp=tp+1
    else:
        c[a]=1 
        cluster1=cluster1+1
        if(belong[a]==c[a]):
            tp=tp+1
   #print(c[a])
    a=a+1
#making clusters
c0array=[[0 for p in range(2)] for q in range(cluster0)]
c1array=[[0 for p in range(2)] for q in range(cluster1)]
a=i=j=0
for row in original3: 
    if(c[a]== 0):
        c0array[i][0]=row[0]
        c0array[i][1]=row[1]
        i=i+1
    if(c[a]== 1):
        c1array[j][0]=row[0]
        c1array[j][1]=row[1]
        j=j+1
    a=a+1
aaaa=pd.DataFrame(c0array)     
cccc=pd.DataFrame(c1array)     

d=[[0 for p in range(2)] for q in range(cluster1)]

#validity indexes
fcpi_3=validations.fCPI(u,belong)
fintra_3=validations.Intra(original3,c,cluster0,cluster1)
finter_3=validations.Inter(original3,c,cluster0,cluster1)
fsi_3 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
fmse_3=validations.MSE(c,belong)
fdi_3= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)


#PRINTING
'''
print(" ")
print("CASE 1 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%fcpi_1," ","%.4f"%fintra_1," ","%.4f"%finter_1," ","%.4f"%fsi_1," ","%.4f"%fmse_1," ","%.4f"%fdi_1)

print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%fcpi_2," ","%.4f"%fintra_2," ","%.4f"%finter_2," ","%.4f"%fsi_2," ","%.4f"%fmse_1," ","%.4f"%fdi_2)

print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%fcpi_3," ","%.4f"%fintra_3," ","%.4f"%finter_3," ","%.4f"%fsi_3," ","%.4f"%fmse_1," ","%.4f"%fdi_3)

'''