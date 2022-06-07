# libreria numpy

import numpy as np

a = np.array(
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
)

print(a,'\n')

'''
row_r1 = a[1,:]
row_r2 = a[1:2,:]
print(row_r1,row_r1.shape,'\n')
print(row_r2,row_r2.shape,'\n')
'''

col_l1 = a[:,1]
col_l2 = a[:,1:2]
print(col_l1, col_l1.shape, '\n')
print(col_l2, col_l2.shape, '\n')
