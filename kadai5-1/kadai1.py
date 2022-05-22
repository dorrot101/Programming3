import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path

def hyperbola(x, y, ch, sample, ratio):
    section = np.zeros((ratio, ratio))
    tx = x+1; ty = y+1
    
    if(x == np.shape(sample)[0]-1): tx = x
    if(y == np.shape(sample)[1]-1): ty = y
    
    for i in range(ratio):
        for j in range(ratio):
            section[i,j] = sample[x,y,ch]*(i-ratio)*(j-ratio)/pow(ratio,2) - sample[tx,y,ch]*(i)*(j-ratio)/pow(ratio,2) - sample[x,ty,ch]*(i-ratio)*(j)/pow(ratio,2) + sample[tx,ty,ch]*(i)*(j)/pow(ratio,2)
               
    return section

def resizeIMG(filename, ratio):
    images = Image.open(filename)
    imgnp = np.array(images)
    x, y, dim = np.shape(images)
    RESIZEDIMG = np.zeros((ratio*x,ratio*y,dim),dtype=int)
    for i in range(x):
        for j in range(y):
            RESIZEDIMG[ratio*i,ratio*j,:] = imgnp[i,j,:]

    for i in range(x):
        for j in range(y):
            for k in range(dim):
                RESIZEDIMG[ratio*i:ratio*(i+1), ratio*j:ratio*(j+1), k] = hyperbola(i, j, k, imgnp, ratio)
                

    plt.imshow(RESIZEDIMG)
    savename = Path(filename).stem + '_' + str(ratio)
    plt.savefig(savename)



filename = './images/Lenna32.png'
resizeIMG(filename, 4)
resizeIMG(filename, 8)

filename = './images/Lenna64.png'
resizeIMG(filename, 4)
resizeIMG(filename, 8)



