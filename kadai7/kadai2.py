import csv 
import numpy as np
import matplotlib.pyplot as plt

def basis(j,k,t,Data,sector):
    if(k == 0): 
        if(sector[j]<=Data[t] and Data[t]<sector[j+1]):
            return 1
        else:
            return 0 
    else:
        return ((Data[t]-sector[j])*basis(j,k-1,t,Data,sector))/(sector[j+k]-sector[j]) + ((sector[j+k+1]-Data[t])*basis(j+1,k-1,t,Data,sector))/(sector[j+k+1]-sector[j+1])

csv_source = open('bikesharing.csv','r',encoding='utf-8')
csv_file = csv.reader(csv_source)
next(csv_file)
data = []
for line in csv_file:
    line = list(map(float, line))
    data.append(line)
csv_source.close()
data = np.array(data)


LowerBound = 0
UpperBound = 1
Y = data[:,14]
real_X = data[:,0]
Data = (real_X-1)/(np.shape(data)[0]-1) # normalize data
DataNum = np.shape(Data)[0] # Get Number of data
plt.scatter(Data,Y)
#plt.savefig('scatter')
plt.show()
for dim in range(2,4): # 2,3-dimension
    for NodeNum in range(11,31,10): # Number of node is 11, 21
        thislabel = ''
        A = np.zeros((DataNum,NodeNum))
        Nodesector = np.linspace(LowerBound,UpperBound,NodeNum,endpoint='True')
        j = NodeNum - dim - 2
        for iter_j in range(j+1):
            for iter_t in range(DataNum):
                A[iter_t, iter_j]= basis(iter_j,dim,iter_t,Data,Nodesector)
        result = np.linalg.pinv(np.transpose(A)@A)@np.transpose(A)@Y
        thislabel = 'b_('+str(NodeNum)+','+str(dim)+')'
        
        plt.plot(Data,A@result,label=thislabel)
        plt.legend()
        #plt.savefig(thislabel)
        plt.show()
