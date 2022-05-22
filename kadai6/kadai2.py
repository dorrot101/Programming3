from operator import indexOf
from xml.etree.ElementPath import find
import numpy as np
import math 
from numpy.linalg import multi_dot

A = np.array([[1,4],[2,3]])

w,v = np.linalg.eig(A)
if(np.min(abs(v)) != 0):
    v = v / np.min(abs(v), axis = 0)
eigenvalvector = np.array([-1,5])
eigenvecmatrix = np.array([[-2, 1],[1,1]])

print('w : ', w)
print('eigenvalvector : ',eigenvalvector)
print('v : \n', v)
print('eigenvecmatrix : \n',eigenvecmatrix)