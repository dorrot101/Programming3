from trace import Trace
import numpy as np
import math 
from numpy.linalg import multi_dot

A = np.array([[1,4],[2,3]])
eigenvalvector = np.array([-1,5])
eigenvecmatrix = np.array([[-2, 1],[1,1]])
print('A = \n', A)
print('eigenvalvector = ',eigenvalvector)
print('eigenvecmatrix = \n',eigenvecmatrix)


# 1-1
left = A @ eigenvecmatrix
print('A @ eigenvecmatrix = \n',left)
right = eigenvecmatrix * eigenvalvector
print('eigenvecmatrix * eigenvalvector = \n',right)

# 1-2
#Trace of A
Trace_A = np.trace(A)    
#Sum of eigenvalue
sum = np.sum(eigenvalvector)

if(Trace_A == sum):  
    print('Trace_A = ', Trace_A)
    print('sum = ', sum)
    print("Trace of A matrix and sum of eigenvalue are same")
else:   print("Trace of A matrix and sum of eigenvalue are different")

# 1-3
Det_A = np.linalg.det(A)
prodvalue = np.prod(eigenvalvector)

if(math.isclose(Det_A,prodvalue)):  
    print('Det_A = ' ,Det_A)
    print('prodvalue = ', prodvalue)
    print("Determinant of A matrix and product of eigenvalue are same")
else:   print("Determinant of A matrix and product of eigenvalue are different")