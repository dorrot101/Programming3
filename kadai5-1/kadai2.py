import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path
import math 

def spline3(sample,fixed,ch,num,ratio,axis):    
    parameters = np.zeros((4*num,4*num))
    y = np.zeros((4*num,1))
    
    for i in range(num):
        if(axis == 0):
            if(i == num-1):
                y[4*i:4*i+2] = np.array([sample[fixed,ratio*i,ch],sample[fixed,ratio*i,ch]]).reshape(2,1)
            else:
                y[4*i:4*i+2] = np.array([sample[fixed,ratio*i,ch],sample[fixed,ratio*(i+1),ch]]).reshape(2,1)
        elif(axis == 1):
            if(i == num-1):
                y[4*i:4*i+2] = np.array([sample[ratio*i,fixed,ch],sample[ratio*i,fixed,ch]]).reshape(2,1)    
            else:
                y[4*i:4*i+2] = np.array([sample[ratio*i,fixed,ch],sample[ratio*(i+1),fixed,ch]]).reshape(2,1)    

    for i in range(num):            
        for j in range(4):
            parameters[4*i, 4*i+j] = pow(ratio*i,3-j)
            parameters[4*i+1, 4*i+j] = pow(ratio*(i+1),3-j)            
            if(i>0):
                if(j<3):
                    parameters[4*i+2,4*(i-1)+j] = (3-j)*pow(ratio*i,2-j)
                    parameters[4*i+2,4*i+j] = (j-3)*pow(ratio*i,2-j)
                if(j<2):
                    parameters[4*i+3,4*(i-1)+j] = math.factorial(3-j)*pow(ratio*i,1-j)
                    parameters[4*i+3,4*i+j] = -math.factorial(3-j)*pow(ratio*i,1-j)
    
    for j in range(2):
        parameters[2,j] = math.factorial(3-j)*pow(0,1-j)
        parameters[3,4*(num-1)+j] = math.factorial(3-j)*pow(ratio*num,1-j)       
    
    A = np.linalg.solve(parameters,y)
    result = np.zeros(ratio*(num))
    
    for i in range(num):
        src = np.arange(ratio*i,ratio*(i+1),1)
        y = A[4*i]*pow(src,3)+A[4*i+1]*pow(src,2)+A[4*i+2]*pow(src,1)+A[4*i+3]
        result[ratio*i:ratio*(i+1)] = y
        
    return result

def SplineInterpolation(filename,ratio,axis):
    sample = Image.open(filename)
    imgnp = np.array(sample)
    x,y,ch = np.shape(imgnp)
    RESIZEDIMG = np.zeros((ratio*x,ratio*y,ch),dtype=int)
    
    for collum in range(x):
        for row in range(y):
            RESIZEDIMG[ratio*collum,ratio*row,:] = imgnp[collum,row,:]
    if(axis == 0):
        for collum in range(x):
            for rgb in range(ch):
                colindex = ratio*collum
                RESIZEDIMG[colindex,:,rgb] = spline3(RESIZEDIMG,colindex,rgb,x,ratio,0)
        for row in range(y):
            for rowiter in range(ratio):
                for rgb in range(ch):
                    rowindex = ratio*row+rowiter
                    RESIZEDIMG[:,rowindex,rgb] = spline3(RESIZEDIMG,rowindex,rgb,y,ratio,1)           
    elif(axis == 1):
        for row in range(y):
            for rgb in range(ch):
                rowindex = ratio*row
                RESIZEDIMG[:,rowindex,rgb] = spline3(RESIZEDIMG,rowindex,rgb,y,ratio,1)
        for collum in range(x):
            for coliter in range(ratio):
                for rgb in range(ch):
                    colindex = ratio*collum+coliter
                    RESIZEDIMG[colindex,:,rgb] = spline3(RESIZEDIMG,colindex,rgb,x,ratio,0)
    
    plt.imshow(RESIZEDIMG)
    savename = Path(filename).stem + '_' + str(ratio) 
    if(axis == 1): savename = savename + '_col'
    elif(axis == 0): savename = savename + '_row'
    plt.savefig(savename)

filename = './images/Lenna32.png'
SplineInterpolation(filename, 4, 0)
SplineInterpolation(filename, 8, 0)
SplineInterpolation(filename, 4, 1)
SplineInterpolation(filename, 8, 1)

filename = './images/Lenna64.png'
SplineInterpolation(filename, 4, 0)
SplineInterpolation(filename, 8, 0)
SplineInterpolation(filename, 4, 1)
SplineInterpolation(filename, 8, 1)
