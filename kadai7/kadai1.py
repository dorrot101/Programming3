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

NodeNum = 11
Dimension = 4
LowerBound = 0
UpperBound = 1
Nodesector = np.linspace(LowerBound,UpperBound,NodeNum,endpoint='True')
Data = np.linspace(LowerBound,UpperBound,101,endpoint='True')
DataNum = np.shape(Data)[0]

for dim in range(Dimension+1):
    j = NodeNum - dim - 2
    thislabel = ''
    for iter_j in range(j+1):
        Y = np.zeros(DataNum)
        for iter_data in range(DataNum):
            Y[iter_data] += basis(iter_j,dim,iter_data,Data,Nodesector)
        #thislabel = 'b_('+str(iter_j)+','+str(dim)+')'
        plt.plot(Data,Y,label=thislabel)
        plt.legend()
    #plt.savefig(thislabel)
    plt.show()
    
    
    
    