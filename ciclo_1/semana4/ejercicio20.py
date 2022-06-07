# libreria numpy

import numpy as np

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
y = np.array([1,0,1])

z = np.empty_like(x)

print(x,'\n')
print(z,'\n')

for i in range(4):
    z[i,:] = x[i,:] + y

print(z)