import math,struct

def EuclideanDistance(point, centroid):
    result = 0

    result +=  pow(point[0] - centroid[0], 2)
    result +=  pow(point[1] - centroid[1], 2)

    result = math.sqrt(result)
    return result

def EuclideanDistanceFour(point, centroid):
    result = 0

    result +=  pow(point[0] - centroid[0], 2)
    result +=  pow(point[1] - centroid[1], 2)
    result +=  pow(point[2] - centroid[2], 2)
    result +=  pow(point[3] - centroid[3], 2)

    result = math.sqrt(result)
    return result


def ManhattanDistance(point, centroid):
    result = 0

    result +=  abs(point.x - centroid.x)
    result +=  abs(point.y - centroid.y)

    return result

def Intra(original,c,cluster0,cluster1):
    avg = 0
    intra1 =  0
    a = 0
    for row in original: 
        if(c[a] ==  0):
            b = a+1
            for row2 in range(b,156):
                if(c[b]  ==  c[a]):
                    dis = math.sqrt((row[0]-original[row2][0])**2+(row[1]-original[row2][1])**2)
                    #dis = EuclideanDistance(row,original[row2]) 
                    intra1 = intra1 + dis
                    avg = avg + 1        
                b = b+1
        a = a+1           
    intra1 = intra1/cluster0 
    
    avg = 0
    intra2 =  0
    a = 0
    for row in original: 
        if(c[a] ==  1):
            b = a+1
            for row2 in range(b,156):
                if(c[b]  ==  1):
                    dis = math.sqrt((row[0]-original[row2][0])**2+(row[1]-original[row2][1])**2)
                    dis2 = 1
                    intra2 = intra2 + dis
                    avg = avg + dis2        
                b = b+1
        a = a+1       
    intra2 = intra2/cluster1
    intra =  (intra1+intra2)/2
    return intra

def Inter(original,c,cluster0,cluster1):
    avg = 0
    inter1 =  0
    a = 0
    for row in original: 
        if(c[a] ==  0):
            b = a+1
            for row2 in range(b,156):
                p = b
                if(c[p]  ==  1):
                    dis = math.sqrt((row[0]-original[row2][0])**2+(row[1]-original[row2][1])**2)
                    inter1 = inter1 + dis
                    avg = avg + 1        
                p = p+1
        a = a+1       
    inter1 = inter1/cluster0
    avg = 0
    inter2 =  0
    a = 0
    for row in original: 
        if(c[a] ==  1):
            b = a+1
            for row2 in range(b,156):
                if(c[b]  ==  0):
                    dis = math.sqrt((row[0]-original[row2][0])**2+(row[1]-original[row2][1])**2)
                    inter2 = inter2 + dis
                    avg = avg + 1        
                b = b+1
        a = a+1       
    inter2 = inter2/cluster1
    inter =  (inter1+inter2)/2
    return inter
    
def CPI(d,belong):
    a = cluster1 = cluster0 = tp = w = 0
    c = [0 for q in range(156)]
    for row in d:
        w = w+1
        if(row[0]>row[1]):
            c[a] = 1
            cluster1 = cluster1+1 
            if(belong[a] == c[a]):
                tp = tp+1
        else:
            c[a] = 0 
            cluster0 = cluster0+1
            if(belong[a] == c[a]):
                tp = tp+1
        a = a+1
    cpi = (tp/156.0)
    return cpi
def fCPI(d,belong):
    return 1
'''
def fCPI(d,belong):
    a = cluster1 = cluster0 = tp = w = 0
    c = [0 for q in range(156)]
    for row in d:
        w = w+1
        if(row[0]<row[1]):
            c[a] = 1
            cluster1 = cluster1+1 
            if(belong[a] == c[a]):
                tp = tp+1
        else:
            c[a] = 0 
            cluster0 = cluster0+1
            if(belong[a] == c[a]):
                tp = tp+1
        a = a+1
    cpi = (tp/156.0)
    return cpi
'''
def Silhouette(c0array,c1array,cluster0,cluster1):
    sum_si = 0
    for row1 in c0array:
        sumDis_A = 0
        sumDis_B = 0
        for row2 in c0array:
            if(row1!= row2):
                dis = EuclideanDistance(row1,row2)
                sumDis_A = sumDis_A+dis
        ai = sumDis_A/(cluster0-1)
        for row2 in c1array:
            dis = EuclideanDistance(row1,row2)
            sumDis_B = sumDis_B+dis
        bi = sumDis_B/(cluster1)
        if(ai>bi):
            si = (bi-ai)/ai
        else:
            si = (bi-ai)/bi
        sum_si = sum_si+si
    
    for row1 in c1array:
        sumDis_A = 0
        sumDis_B = 0
        for row2 in c1array:
            if(row1!= row2):
                dis = EuclideanDistance(row1,row2)
                sumDis_A = sumDis_A+dis
                
        ai = sumDis_A/(cluster1-1)
        for row2 in c0array:
            dis = EuclideanDistance(row1,row2)
            sumDis_B = sumDis_B+dis
        bi = sumDis_B/cluster0
        if(ai>bi):
            si = (bi-ai)/ai
        else:
            si = (bi-ai)/bi
        sum_si = sum_si+si
    
    si=sum_si/156
    return si

def MSE(c,belong):
    sums = 0
    for i in range(156):
        sums=sums+((c[i]-belong[i])**2)
    res = sums/156
    return res

def DunnIndex(c0array,c1array,centroids,cluster0,cluster1):
    mx1=0
    mx2=0
    for i in c0array:
        for j in c0array:
            dis =EuclideanDistance(i,j)
            mx1=mx1+dis
    mx1=mx1/cluster0        
    for i in c1array:
        for j in c1array:
            dis =EuclideanDistance(i,j)
            mx2=mx2+dis
    mx2=mx2/cluster1        
    mx=max(mx1,mx2)        
    mn=999
    for i in c0array:
        for j in c1array:
            dis =EuclideanDistance(i,j)
            if mn>dis:
                mn=dis
    di = mn/mx
    return di        
            

def hammingdistance1(a,b,c,d):
  rtrn1 = []
  rtrn2=[]
  a = struct.pack('d', a)
  b = struct.pack('d', b)
  c = struct.pack('d', c)
  d= struct.pack('d', d)
  '''
  e = struct.pack('d', a)
  f = struct.pack('d', b)
  g = struct.pack('d', a)
  h = struct.pack('d', b)
  '''
  for ba, bb,bc,bd in zip(a, b,c,d):
    rtrn1.append(ba ^ bc)
    rtrn2.append(bb ^ bd)

  return struct.unpack('d', bytes(rtrn1))[0]+struct.unpack('d', bytes(rtrn2))[0]


def hammingdistance2(a,b,c,d,e,f,g,h):
  rtrn1 = []
  rtrn2=[]
  rtrn3= []
  rtrn4=[]
  
  
  a = struct.pack('d', a)
  b = struct.pack('d', b)
  c = struct.pack('d', c)
  d=  struct.pack('d', d)
  e = struct.pack('d', e)
  f = struct.pack('d', f)
  g = struct.pack('d', g)
  h = struct.pack('d', h)
  for ba, bb,bc,bd,be,bf,bg,bh in zip(a, b,c,d,e,f,g,h):
    rtrn1.append(ba ^ be)
    rtrn2.append(bb ^ bf)
    rtrn3.append(bc ^ bg)
    rtrn4.append(bd ^ bh)

  return struct.unpack('d', bytes(rtrn1))[0]+struct.unpack('d', bytes(rtrn2))[0]+struct.unpack('d', bytes(rtrn3))[0]+struct.unpack('d', bytes(rtrn4))[0]
