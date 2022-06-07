# libreria numpy

import numpy as np

a = np.array(
    [
        [1,2,3],
        [5,6,7],
        [9,10,11],
    ]
)

print(a, '\n')

'''
b = a[:2, 1:3]
print(b,'\n')

c = a[1:3,:2]
print(c)
'''

d = np.fliplr(a)
print(d)

d = np.flip(a)
print(d)