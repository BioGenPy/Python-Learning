import numpy as np
print("-----------NumPy Creating Arrays--------")
arr = np.array([1,2,3,4,5,6])
print(arr)

print(type(arr))

print("-----------0-D Arrays----------")
import numpy as np 
arr = np.array(34)
print(arr)

print("-----------1-D Arrays----------")

prr = np.array([1,2,3,4,5,4,7])
print(prr)

print("-----------2-D Arrays----------")
ddarray = np.array([[1,2,3],[4,5,6]])
print(ddarray)

print("-----------3-D arrays----------")

dddarry = np.array([  [1,2,3], [4,5,6], [1,2,3],[4,5,6]   ])
print(dddarry)


a = np.array(35)
b = np.array([1,2,3,4,5])
c = np.array([ [1,2,3],[4,5,6] ])
d = np.array([[  [1,2,3], [4,5,6], [1,2,3 ], [4,5,6 ] ] ])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print("-----------Higher Dimensional Arrays----------")

higharry = np.array([1,2,3,4],ndmin=5 )
print(arr)
print('number of dimesnsions :',arr.ndim)
"""In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array."""
