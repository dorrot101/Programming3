import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, sample):
    n = np.shape(sample)[0]
    sum = np.zeros(np.shape(x)[0])
    
    for iter in range(n):
        k = 0
        l_x = np.ones(np.shape(x)[0])
        l_kx = 1.0
        x_k = sample[iter,0]
        for i in range(n):
            if(iter == i): 
                continue
            l_x *= x - sample[i,0]
            l_kx *= x_k - sample[i,0]
        k = (l_x/l_kx)*(sample[iter,1])
        sum += k
    return sum

# 1-1
# set sample
x = np.arange(-1,1,0.01)
samples = np.array([[-0.6,-0.3],[-0.1, 0.5],[0.5, 0.1]])
# get parameter of lagrange interpolation
y = lagrange(x, samples)
# adjust plot option
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.plot(x,y)
plt.scatter(samples[:,0],samples[:,1])
plt.savefig("test1.png")
plt.clf()

# 1-2
# set sample
samples = np.array([[-0.6, -0.25],[-0.4, 0.3],[0.0, 0.3],[0.1, -0.25],[0.5, -0.2]])
# get parameter of lagrange interpolation
y = lagrange(x, samples)
# adjust plot option
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.plot(x,y)
plt.scatter(samples[:,0],samples[:,1])
plt.savefig("result1.png")
plt.show()