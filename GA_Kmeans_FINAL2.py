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

    normData.to_csv('dataset/ga_case2w.csv', index=None, header=None)
    return normData


data = pd.read_csv('dataset/ga_case2.csv', header=None)
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

# Kmeans Algorithm Start

c1= [0.682,121.080]
c2 = [0.9853,128.72]
count=0
centroids=[c1,c2]

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
gcpi_2=validations.fCPI(d,belong)
gintra_2=validations.Intra(original2,c,cluster0,cluster1)
ginter_2=validations.Inter(original2,c,cluster0,cluster1)
gsi_2 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
gmse_2=validations.MSE(c,belong)
gdi_2= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)

'''
print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%fcpi_2," ","%.4f"%fintra_2," ","%.4f"%finter_2," ","%.4f"%fsi_2," ","%.4f"%fmse_2," ","%.4f"%fdi_2)
'''