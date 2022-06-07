# libreria numpy - matrices booleanas

import numpy as np

a =  np.array(
    [
        [1,2],
        [3,4],
        [5,6]
    ]
)

print(a,'\n')

bool_idx = (a > 2)
print(bool_idx)

print(bool_idx.all())
print(bool_idx.any())

print(a[bool_idx])
print(a[a > 2])
