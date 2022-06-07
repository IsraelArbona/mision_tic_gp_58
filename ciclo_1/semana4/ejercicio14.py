# libreria numpy - indexación de matrices de enteros

import numpy as np

a = np.array(
    [
        [1,2],
        [3,4],
        [5,6]
    ]
)

print(a.shape)
print(a[[0,1,2],[0,1,0]])
print(np.array([a[0,0],a[1,1],a[2,0]]))
print(a[[0,0,0,0,0],[1,1,1,1,1]])
print(np.array([a[0,1],a[0,1],a[0,1],a[0,1],a[0,1]]))