# libreria numpy

import numpy as np

a = np.array([1,2])
#print(a.dtype)
b = np.array([1.0,2.0])
#print(b.dtype)

c = np.array([1,2], dtype=np.float64)
print(c.dtype)

d = np.array([1.0,2.0], dtype=np.str0)
print(d.dtype)
print(d)
