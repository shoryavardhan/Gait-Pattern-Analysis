import random
import numpy as np
import pandas as pd
import Validations_FINAL as validations
import math

#DATASET
dataset=pd.read_csv("dataset/norm.csv")
original_68=dataset.iloc[0:68,1:5].values 
original_88=dataset.iloc[0:88,1:5].values 
original=dataset.iloc[0:156, 1:5].values #case3
belong = dataset.iloc[0:156,9].values 

# print("PSO with KMeans Algorithm")

W = 0.5
c1 = 0.8
c2 = 0.9 

n_iterations = 50
target_error = 10e-5
n_particles = 50

#random            
f1c = open('dataset/case1_cp88.csv')
f1i = open('dataset/case1_intact68.csv')

class Particle():
    def __init__(self):
        #case 2 - cp - 88
        offset = random.randrange(156)
        f1c.seek(offset)     
        f1c.readline()                  
        random_line1 = f1c.readline()
        arr= [0.0,0.0,0.0,0.0]
        arr= random_line1.split(',')
        cp0=float(arr[0])
        cp1=float(arr[1])
        cp2=float(arr[2])
        cp3=float(arr[3])
        #case3 - intact - 68
        offset = random.randrange(156)
        f1i.seek(offset)     
        f1i.readline()                  
        random_line1 = f1i.readline()
        arr= [0.0,0.0,0.0,0.0]
        arr= random_line1.split(',')
        in0=float(arr[0])
        in1=float(arr[1])
        in2=float(arr[2])
        in3=float(arr[3])
        #cp0=cp1=in0=in1=(-1) ** (bool(random.getrandbits(1))) * random.random()*50
        self.position = np.array([cp0,cp1,cp2,cp3,in0,in1,in2,in3])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0,0,0,0,0,0,0,0])
        
    def __str__(self):
        print("I am at ", self.position, " my pbest is ", self.pbest_position)
    
    def move(self):
        self.position = self.position + self.velocity


class Space():
    def __init__(self, target, target_error, n_particles):
        self.target = target
        self.target_error = target_error
        self.n_particles = n_particles-1
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random()*50, random.random()*50, random.random()*50, random.random()*50,
                                        random.random()*50, random.random()*50, random.random()*50, random.random()*50])

    def printing(self):
        for particle in self.particles:
            particle.__str__()
   
    def fitness(self, particle):
        sq_sumcp=sq_sumintact=0
        for row in original_88:
            sq_sumcp = sq_sumcp+ math.sqrt((particle.position[0]-row[0])**2+(particle.position[1]-row[1])**2
                                           +(particle.position[2]-row[2])**2+(particle.position[3]-row[3])**2)
        for row in original_68:
            sq_sumintact = sq_sumintact+ math.sqrt((particle.position[4]-row[0])**2+(particle.position[5]-row[1])**2+
                                                   (particle.position[6]-row[2])**2+(particle.position[7]-row[3])**2)
        sum=((sq_sumcp/88)+(sq_sumintact/68))/2
        return sum
    
    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if(particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position
            

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if(self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for particle in self.particles:
            global W
            new_velocity = (W*particle.velocity) + (c1*random.random())*validations.hammingdistance2(particle.pbest_position[0],particle.pbest_position[1],particle.pbest_position[2],particle.pbest_position[3],particle.position[0],particle.position[1],particle.position[2],particle.position[3]) + \
                            (random.random()*c2) *  validations.hammingdistance2(self.gbest_position[0],self.gbest_position[1],self.gbest_position[2],self.gbest_position[3],particle.position[0],particle.position[1],particle.position[3],particle.position[4])
            particle.velocity = new_velocity
            particle.move()
            

search_space = Space(0, target_error, n_particles)
particles_vector = [Particle() for p in range(search_space.n_particles)]
part = Particle()
part.position=np.array([59.56, 0.5475, 59.56, 67.5625,130.98013, 131.82135, 3.21945, 3.65202])
particles_vector.append(part)
search_space.particles = particles_vector
#search_space.printing()

iteration = 0
while(iteration < n_iterations):
    search_space.set_pbest()    
    search_space.set_gbest()

    if(abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
        break

    search_space.move_particles()
    iteration += 1
    
    
#print("\n The best solution is: \n", search_space.gbest_position, "\n in" ,iteration, " iterations")
c1 = np.array([0.0,0.0,0.0,0.0])
c2 = np.array([0.0,0.0,0.0,0.0])
c1[0]= search_space.gbest_position[0]
c1[1]= search_space.gbest_position[1]
c1[2]= search_space.gbest_position[2]
c1[3]= search_space.gbest_position[3]
c2[0]= search_space.gbest_position[4]
c2[1]= search_space.gbest_position[5]
c2[2]= search_space.gbest_position[6]
c2[3]= search_space.gbest_position[7]
'''
print("\nCentroid 1:")
print(c1)
print("\nCentroid 2:")
print(c2)
print("\n")
'''
################Kmeans start

#initialising centroids for the first time
count=0
centroids=[c1,c2]

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
for row in original: 
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
hcpi_1=validations.CPI(d,belong)
hintra_1=validations.Intra(original,c,cluster0,cluster1)
hinter_1=validations.Inter(original,c,cluster0,cluster1)
hsi_1 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
hmse_1=validations.MSE(c,belong)
hdi_1= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)

#PRINTING

'''
print(" ")
print("CASE 1 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%hcpi_1," ","%.4f"%hintra_1," ","%.4f"%hinter_1," ","%.4f"%hsi_1," ","%.4f"%hmse_1," ","%.4f"%hdi_1)

print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%hcpi_2," ","%.4f"%hintra_2," ","%.4f"%hinter_2," ","%.4f"%hsi_2," ","%.4f"%hmse_2," ","%.4f"%hdi_2)

print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%hcpi_3," ","%.4f"%hintra_3," ","%.4f"%hinter_3," ","%.4f"%hsi_3," ","%.4f"%hmse_3," ","%.4f"%hdi_3)
'''
