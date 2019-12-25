import pandas as pd
import random
import numpy as np
from genetic import Genetic
from cluster import Clustering
import Validations_FINAL as validations
import math
#DATASET
dataset=pd.read_csv("dataset/norm.csv")
original=dataset.iloc[0:156,1:5].values   #case1 
original2=dataset.iloc[0:156, [1,2]].values #case2
original3=dataset.iloc[0:156, [5,6]].values #case3 
belong = dataset.iloc[0:156,9].values 

class Generation:
    def __init__(self, numberOfIndividual, generationCount):
        self.numberOfIndividual = numberOfIndividual
        self.chromosomes = []
        self.generationCount = generationCount

    def sortChromosomes(self):
        self.chromosomes = sorted(
            self.chromosomes, reverse=True, key=lambda elem: elem.fitness)
        return self.chromosomes

    def randomGenerateChromosomes(self, lengthOfChromosome):
        for i in range(0, self.numberOfIndividual):
            chromosome = Chromosome([], lengthOfChromosome)
            chromosome.randomGenerateChromosome()
            self.chromosomes.append(chromosome)
            #print(chromosome.genes)

class Chromosome:
    def __init__(self, genes, length):
        self.genes = genes
        self.length = length
        self.fitness = 0

    def randomGenerateChromosome(self):
        for i in range(0, self.length, +1):
            gen = float('%.2f' % random.uniform(0.2, 1.2))
            #print(gen)
            self.genes.append(gen)

        return self

def minmax(data):
    normData = data
    data = data.astype(float)
    normData = normData.astype(float)
    for i in range(0, data.shape[1]):
        tmp = data.iloc[:, i]
        # max of each column
        maxElement = np.amax(tmp)
        # min of each column
        minElement = np.amin(tmp)

        # norm_dat.shape[0] : size of rows
        for j in range(0, normData.shape[0]):
            normData[i][j] = float(
                data[i][j] - minElement) / (maxElement - minElement)

    normData.to_csv('dataset/ga_case3w.csv', index=None, header=None)
    return normData


data = pd.read_csv('dataset/ga_case3.csv', header=None)
data = minmax(data)

# size of column
dim = data.shape[1]
#print(dim)

# kmeans parameters & GA parameters
generationCount = 0
budget= 5
kmax =2
numOfInd = 5
Ps = 0.2
Pm = 0.01
Pc = 0.8
'''
print("-------------GA Info-------------------")
print("budget", budget)
print("kmax", kmax)
print("numOfInd", numOfInd)
print("Ps", Ps)
print("Pm", Pm)
print("Pc", Pc)
print("---------------------------------------")
'''
# dim or pattern id 
chromosome_length = kmax * dim

#-------------------------------------------------------#
# 							main 						#
#-------------------------------------------------------#
initial = Generation(numOfInd, 0)
initial.randomGenerateChromosomes(chromosome_length)  # initial generate chromosome
clustering = Clustering(initial, data, kmax)  # eval fit of chromosomes

# ------------------calc fitness------------------#
generation = clustering.calcChromosomesFit()

# ------------------------GA----------------------#
while generationCount <= budget:
    GA = Genetic(numOfInd, Ps, Pm, Pc, budget, data, generationCount, kmax)
    generation, generationCount = GA.geneticProcess(generation)
    iBest = generation.chromosomes[0]
    #clustering.printIBest(iBest)

#clustering.output_result(iBest, data)

c1=[3.598,4.425]
c2=[3.783,4.582]

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
centroids=[c1,c2]
#validity indexes
gcpi_3=validations.fCPI(u,belong)
gintra_3=validations.Intra(original3,c,cluster0,cluster1)
ginter_3=validations.Inter(original3,c,cluster0,cluster1)
gsi_3 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
gmse_3=validations.MSE(c,belong)
gdi_3= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)
'''
print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%gcpi_3," ","%.4f"%gintra_3,"   ","%.4f"%ginter_3,"  ","%.4f"%gsi_3,"  ","%.4f"%gmse_3," ","%.4f"%(gdi_3*10))
'''