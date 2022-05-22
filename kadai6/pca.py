import numpy as np
import math
from numpy.lib.index_tricks import index_exp 
from numpy.linalg import multi_dot

def PCA(data):
    N, d = np.shape(data)
    dimmean = np.sum(data,axis=0)/N
    S = np.zeros((d,d))
    for i in range(d):
        for j in range(d):
            S[i,j] = np.sum(np.dot((data[:,i]-dimmean[i]),(data[:,j]-dimmean[j])))/N
    eigV, eigM = np.linalg.eig(S)
    np.round(eigV,4,eigV)
    np.round(eigM,4,eigM)
    
    proportion = eigV/sum(eigV)
    Z = (data-dimmean) @ eigM    
        
    ordinal = ['1st','2nd','3rd']
    for componentindex in range(d):
        print(ordinal[componentindex],'component equation :')
        for iter in range(N):
            print('%+f = ' % Z[iter,componentindex], end="")
            for yiter in range(d-1):
                print('%+.4f*(%d-%.1f)'% (eigM[componentindex,yiter], data[iter,yiter],dimmean[yiter]), end="") 
            print('%+.4f*(%d-%.1f)'% (eigM[componentindex,d-1], data[iter,d-1],dimmean[d-1]))
    print(Z)
    for iter in range(d): 
        print(ordinal[iter],'proportion : ',proportion[iter])
        print(ordinal[iter],'cumulative proportion : ',sum(proportion[0:iter+1]))

    return proportion ,Z

surveydata = np.array([[8,9,4],[2,5,7],[8,5,6],[3,5,4],[7,4,9],[4,3,4],[3,6,8],[6,8,2],[5,4,5],[6,7,6]])
proportion, principle_component = PCA(surveydata)
maxes = np.max(principle_component, axis = 0)
maxindex = np.transpose(np.array(np.where(principle_component == maxes)))
mines = np.min(principle_component, axis = 0)
minindex = np.transpose(np.array(np.where(principle_component == mines)))

