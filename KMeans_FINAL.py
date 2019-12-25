#LIBRARY
import pandas as pd
import Validations_FINAL as validations

#DATASET
dataset=pd.read_csv("dataset/norm.csv")
original=dataset.iloc[0:156,1:5].values   #case1 
original2=dataset.iloc[0:156, [1,2]].values #case2
original3=dataset.iloc[0:156, [7,8]].values #case3 
belong = dataset.iloc[0:156,9].values 


##################################-----##################################
################################ case1 ##################################
################################-----####################################

#initialising centroids for the first time
count=0
centroids=[[0.85,108.3,0.88,13],[1.38,	124.68	,0.64	,9]]

n=0
while(n<100):
    #calculating d first time
    r=0
    c=0
    row,col=(156,2)
    d=[[0 for p in range(col)] for q in range(row)]
    for row in original:
        c=0
        for cent in centroids:
           d[r][c]=validations.EuclideanDistanceFour(row,cent)
           c=c+1
        r=r+1
        
    # Finding centroids        
    cluster0=0
    cluster1=0 
    i=0   
    sumx1=0
    sumy1=0
    sumx2=0
    sumy2=0
    tp=0
    c=[0 for p in range(156)]
    for dis in d:
        if(dis[1]>dis[0]):
            if(belong[i]==0):
                tp=tp+1
            c[i]=0
            cluster0=cluster0+1
            sumw1=sumy1+original[i][1]
            sumx1=sumx1+original[i][0]
            sumy1=sumy1+original[i][1]
            sumz1=sumy1+original[i][1]
            i=i+1
            
        else:
            if(belong[i]==1):
                tp=tp+1
            c[i]=1
            cluster1=cluster1+1
            sumw2=sumx2+original[i][0]
            sumx2=sumy2+original[i][1]
            sumy2=sumx2+original[i][0]
            sumz2=sumy2+original[i][1]
            i=i+1
    centroids=[[sumw1/cluster0,sumx1/cluster0,sumy1/cluster0,sumz1/cluster0],
               [sumw2/cluster1,sumx2/cluster1,sumy1/cluster1,sumz1/cluster1]]
    n=n+1

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
kcpi_1=validations.CPI(d,belong)
kintra_1=validations.Intra(original,c,cluster0,cluster1)
kinter_1=validations.Inter(original,c,cluster0,cluster1)
ksi_1 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
kmse_1=validations.MSE(c,belong)
kdi_1= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)


##################################-----##################################
################################ case2 ##################################
################################-----####################################

#initialising centroids for the first time
count=0
centroids=[[0.900,0.74875],
[140.166,89.95]]

n=0
while(n<100):
    #calculating d first time
    r=0
    c=0
    row,col=(156,2)
    d=[[0 for p in range(col)] for q in range(row)]
    for row in original2:
        c=0
        for cent in centroids:
           d[r][c]=validations.EuclideanDistance(row,cent)
           c=c+1
        r=r+1
        
    # Finding centroids        
    cluster0=0
    cluster1=0 
    i=0   
    sumx1=0
    sumy1=0
    sumx2=0
    sumy2=0
    tp=0
    c=[0 for p in range(156)]
    for dis in d:
        if(dis[1]>dis[0]):
            if(belong[i]==0):
                tp=tp+1
            c[i]=0
            cluster0=cluster0+1
            sumx1=sumx1+original2[i][0]
            sumy1=sumy1+original2[i][1]
            i=i+1
            
        else:
            if(belong[i]==1):
                tp=tp+1
            c[i]=1
            cluster1=cluster1+1
            sumx2=sumx2+original2[i][0]
            sumy2=sumy2+original2[i][1]
            i=i+1
    
    centroids=[[sumx1/cluster0,sumy1/cluster0],[sumx2/cluster1,sumy2/cluster1]]
    n=n+1

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
kcpi_2=validations.CPI(d,belong)
kintra_2=validations.Intra(original2,c,cluster0,cluster1)
kinter_2=validations.Inter(original2,c,cluster0,cluster1)
ksi_2 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
kmse_2=validations.MSE(c,belong)
kdi_2= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)

##################################-----##################################
################################ case3 ##################################
################################-----####################################

#initialising centroids for the first time
count=0
centroids=[[3.147171999999999, 4.078748787878787],[5.671560533333331, 4.731545777777777]]

n=0
while(n<100):
    #calculating d first time
    r=0
    c=0
    row,col=(156,2)
    d=[[0 for p in range(col)] for q in range(row)]
    for row in original3:
        c=0
        for cent in centroids:
           d[r][c]=validations.EuclideanDistance(row,cent)
           c=c+1
        r=r+1
        
    # Finding centroids        
    cluster0=0
    cluster1=0 
    i=0   
    sumx1=0
    sumy1=0
    sumx2=0
    sumy2=0
    tp=0
    c=[0 for p in range(156)]
    for dis in d:
        if(dis[1]>dis[0]):
            if(belong[i]==0):
                tp=tp+1
            c[i]=0
            cluster0=cluster0+1
            sumx1=sumx1+original3[i][0]
            sumy1=sumy1+original3[i][1]
            i=i+1
            
        else:
            if(belong[i]==1):
                tp=tp+1
            c[i]=1
            cluster1=cluster1+1
            sumx2=sumx2+original3[i][0]
            sumy2=sumy2+original3[i][1]
            i=i+1
    
    centroids=[[sumx1/cluster0,sumy1/cluster0],[sumx2/cluster1,sumy2/cluster1]]
    n=n+1

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

#validity indexes
kcpi_3=validations.CPI(d,belong)
kintra_3=validations.Intra(original3,c,cluster0,cluster1)
kinter_3=validations.Inter(original3,c,cluster0,cluster1)
ksi_3 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
kmse_3=validations.MSE(c,belong)
kdi_3= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)



#PRINTING
'''
print(" ")
print("CASE 1 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%kcpi_1," ","%.4f"%kintra_1," ","%.4f"%kinter_1," ","%.4f"%ksi_1," ","%.4f"%kmse_1," ","%.4f"%kdi_1)

print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%kcpi_2," ","%.4f"%kintra_2," ","%.4f"%kinter_2," ","%.4f"%ksi_2," ","%.4f"%kmse_2," ","%.4f"%kdi_2)

print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%kcpi_3," ","%.4f"%kintra_3," ","%.4f"%kinter_3," ","%.4f"%ksi_3," ","%.4f"%kmse_3," ","%.4f"%kdi_3)

'''