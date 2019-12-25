import random
import numpy as np
import pandas as pd
import Validations_FINAL as validations
import math

#DATASET
dataset=pd.read_csv("dataset/norm.csv")
original2_68=dataset.iloc[0:68,[1,2]].values 
original2_88=dataset.iloc[0:88,[1,2]].values 
original2=dataset.iloc[0:156, [1,2]].values #case2
belong = dataset.iloc[0:156,9].values 

# print("PSO with KMeans Algorithm")

W = 0.5
c1 = 0.8
c2 = 0.9 

n_iterations = 50
target_error = 10e-5
n_particles = 50
#random            
f2c = open('dataset/case2_cp88.csv')
f2i = open('dataset/case2_intact68.csv')

class Particle():
    def __init__(self):
        #case 2 - cp -88
        offset = random.randrange(156)
        f2c.seek(offset)     
        f2c.readline()                  
        random_line1 = f2c.readline()
        arr= [0.0,0.0]
        arr= random_line1.split(',')
        cp0=float(arr[0])
        cp1=float(arr[1])
        #case2 - intact - 68
        offset = random.randrange(156)
        f2i.seek(offset)     
        f2i.readline()                  
        random_line1 = f2i.readline()
        arr= [0.0,0.0]
        arr= random_line1.split(',')
        in0=float(arr[0])
        in1=float(arr[1])
        #cp0=cp1=in0=in1=(-1) ** (bool(random.getrandbits(1))) * random.random()*50
        self.position = np.array([cp0,cp1,in0,in1])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0,0,0,0])
        
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
        self.gbest_position = np.array([random.random()*50, random.random()*50, random.random()*50, random.random()*50])

    def print_particles(self):
        for particle in self.particles:
            particle.__str__()
   
    def fitness(self, particle):
        sq_sumcp=sq_sumintact=0
        for row in original2_88:
            sq_sumcp = sq_sumcp+ math.sqrt((particle.position[0]-row[0])**2+(particle.position[1]-row[1])**2)
        for row in original2_68:
            sq_sumintact = sq_sumintact+ math.sqrt((particle.position[2]-row[0])**2+(particle.position[3]-row[1])**2)
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
            new_velocity = (W*particle.velocity) + (c1*random.random())*(particle.pbest_position - particle.position) + \
                            (random.random()*c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()
            

##################################-----##################################
################################ case2 ##################################
################################-----####################################

search_space = Space(0, target_error, n_particles)
particles_vector = [Particle() for p in range(search_space.n_particles)]
part = Particle()
part.position=np.array([0.845,98.54,1.02,136.84])
particles_vector.append(part)
search_space.particles = particles_vector
#search_space.print_particles()

iteration = 0
while(iteration < n_iterations):
    search_space.set_pbest()    
    search_space.set_gbest()

    if(abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
        break

    search_space.move_particles()
    iteration += 1
    
    
#print("\n The best solution is: \n", search_space.gbest_position, "\n in" ,iteration, " iterations")
c1 = np.array([0.0,0.0])
c2 = np.array([0.0,0.0])
c1[0]= search_space.gbest_position[0]
c1[1]= search_space.gbest_position[1]
c2[0]= search_space.gbest_position[2]
c2[1]= search_space.gbest_position[3]
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
pcpi_2=validations.CPI(d,belong)
pintra_2=validations.Intra(original2,c,cluster0,cluster1)
pinter_2=validations.Inter(original2,c,cluster0,cluster1)
psi_2 = validations.Silhouette(c0array,c1array,cluster0,cluster1)
pmse_2=validations.MSE(c,belong)
pdi_2= validations.DunnIndex(c0array,c1array,centroids,cluster0,cluster1)

#PRINTING
'''
print(" ")
print("CASE 1 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%pcpi_1," ","%.4f"%pintra_1," ","%.4f"%pinter_1," ","%.4f"%psi_1," ","%.4f"%pmse_1," ","%.4f"%pdi_1)

print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%pcpi_2," ","%.4f"%pintra_2," ","%.4f"%pinter_2," ","%.4f"%psi_2," ","%.4f"%pmse_2," ","%.4f"%pdi_2)

print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%pcpi_3," ","%.4f"%pintra_3," ","%.4f"%pinter_3," ","%.4f"%psi_3," ","%.4f"%pmse_3," ","%.4f"%pdi_3)
'''
