from cmath import pi
import math
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



LowerBound = 0
UpperBound = 2*pi
theta = np.arange(LowerBound,UpperBound,pi/50)
cosx = np.cos(theta)
siny = np.sin(theta)
n = np.shape(cosx)[0]

Num = np.array([4,8,16]) # Number of Node is 4,8,16
Dimension = np.array([1,3]) # 1,3 - dimension

for dim in Dimension:
    for NodeNum in Num:
        thislabel = ''
        A = np.zeros((n,NodeNum))
        Nodesector = np.linspace(LowerBound,UpperBound,NodeNum,endpoint='True')
        j = NodeNum - dim - 2
        for iter_j in range(j+1):
            for iter_t in range(n):
                A[iter_t, iter_j]= basis(iter_j,dim,iter_t,theta,Nodesector)
        SinData = np.linalg.pinv(np.transpose(A)@A)@np.transpose(A)@siny
        thislabel = 'b_('+str(NodeNum)+','+str(dim)+')'
        plt.scatter(cosx,siny)
        plt.legend()
        plt.plot(cosx,A@SinData,label=thislabel)
        plt.legend()
        plt.show()