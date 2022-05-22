import numpy as np
import matplotlib.pyplot as plt

def spline1(sample, n):    
    parameters = np.zeros((2*n,2*n))
    y = np.zeros((2*n,1))
    for i in range(n):
        y[2*i:2*(i+1)] = np.array([sample[i,1],sample[i+1,1]]).reshape(2,1)
        parameters[2*i:2*(i+1),2*i:2*(i+1)] = np.array([1,sample[i,0],1,sample[i+1,0]]).reshape(2,2)
    A = np.linalg.solve(parameters,y)
    return A

# 2-1
# set sample and sort sample
samples = np.array([[-0.1, 0.5],[-0.6,-0.3],[0.5, 0.1]])
samples = samples[samples[:,0].argsort()]
# get number of sections and get parameter of 1-spline interpolation
n = np.shape(samples)[0]-1
Y = spline1(samples,n)
# calculate output of each sections
for i in range(n):
    x = np.arange(samples[i,0],samples[i+1,0],0.001)
    y = Y[2*i] + Y[2*i+1]*x
    plt.plot(x,y)
# adjust plot option
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.scatter(samples[:,0],samples[:,1])
plt.savefig("test2.png")
plt.clf()

# 2-2
# set sample and sort sample
samples = np.array([[-0.6, -0.4],[-0.4, 0.6],[0.0, 0.1],[0.1, 0.25],[0.5, -0.2]])
samples = samples[samples[:,0].argsort()]
# get number of sections and get parameter of 1-spline interpolation
n = np.shape(samples)[0]-1
Y = spline1(samples,n)
# calculate output of each sections
for i in range(n):
    x = np.arange(samples[i,0],samples[i+1,0],0.001)
    y = Y[2*i] + Y[2*i+1]*x
    plt.plot(x,y)
# adjust plot option
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.scatter(samples[:,0],samples[:,1])
plt.savefig("result2.png")
plt.show()
plt.clf()