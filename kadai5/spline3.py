import numpy as np
import matplotlib.pyplot as plt
import math

def spline3(sample, n):    
    parameters = np.zeros((4*n,4*n))
    y = np.zeros((4*n,1))
    
    for i in range(n):
        y[4*i:4*i+2] = np.array([sample[i,1],sample[i+1,1]]).reshape(2,1)
        for j in range(4):
            parameters[4*i, 4*i+j] = pow(sample[i,0],3-j)
            parameters[4*i+1, 4*i+j] = pow(sample[i+1,0],3-j)            
            if(i>0):
                if(j<3):
                    parameters[4*i+2,4*(i-1)+j] = (3-j)*pow(sample[i,0],2-j)
                    parameters[4*i+2,4*i+j] = (j-3)*pow(sample[i,0],2-j)
                if(j<2):
                    parameters[4*i+3,4*(i-1)+j] = math.factorial(3-j)*pow(sample[i,0],1-j)
                    parameters[4*i+3,4*i+j] = -math.factorial(3-j)*pow(sample[i,0],1-j)
    
    for j in range(2):
        parameters[2,j] = math.factorial(3-j)*pow(sample[0,0],1-j)
        parameters[3,4*(n-1)+j] = math.factorial(3-j)*pow(sample[n,0],1-j)            
        
    A = np.linalg.solve(parameters,y)

    return A

# 3-1
# set sample and sort sample
samples = np.array([[-0.1, 0.5],[-0.6,-0.3],[0.5, 0.1]])
samples = samples[samples[:,0].argsort()]
# get number of sections and get parameter of 3-spline interpolation
n = np.shape(samples)[0]-1
Y = spline3(samples,n)
# calculate output of each sections
for i in range(n):
    x = np.arange(samples[i,0],samples[i+1,0],0.001)
    y = Y[4*i]*pow(x,3)+Y[4*i+1]*pow(x,2)+Y[4*i+2]*pow(x,1)+Y[4*i+3]
    plt.plot(x,y)
# adjust plot option
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.scatter(samples[:,0],samples[:,1])
plt.savefig("test3.png")
plt.clf()

# 3-2
# set sample and sort sample
samples = np.array([[0.6, -0.4],[-0.4, 0.2],[0.0, -0.1],[0.1, 0.3],[-0.7, -0.9]])
samples = samples[samples[:,0].argsort()]
# get number of sections and get parameter of 3-spline interpolation
n = np.shape(samples)[0]-1
Y = spline3(samples,n)
# calculate output of each sections
for i in range(n):
    x = np.arange(samples[i,0],samples[i+1,0],0.001)
    y = Y[4*i]*pow(x,3)+Y[4*i+1]*pow(x,2)+Y[4*i+2]*pow(x,1)+Y[4*i+3]
    plt.plot(x,y)
# adjust plot option
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.scatter(samples[:,0],samples[:,1])
plt.savefig("result3.png")
plt.show()