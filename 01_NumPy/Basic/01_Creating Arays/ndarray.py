import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

print(".................Create a 0-D array with value 42...................")
arr1 = np.array(42)
print(arr1)

arr2 = np.array([1,2,3,4,56])
print(arr2)

arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)

print(".................3-D arrays...................")
arr4 = np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6]])
print(arr4)

a = np.array(45) # zero dimention
b = np.array([1, 2, 3, 4,5])  # one dimention
c = np.array([[1, 2, 3], [4, 5, 6]])  # two dimention
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  # three dimention

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("..............Higher Dimensional Arrays.................")

hda = np.array([1,2,3,4,],  ndmin = 5 )
print(hda)
print('Number of dimensions :', hda.ndim) 
