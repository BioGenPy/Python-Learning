import numpy as np

print("----Reshape From 1-D to 2-D----")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

print(".......Reshape From 1-D to 3-D.....")
print(".......Convert the following 1-D array with 12 elements into a 3-D array......")
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr1.reshape(2,3,2)
print(newarr1)

print("Can We Reshape Into any Shape?")
print("yes")

# arr2 = np.array([1,2,3,4,5,6,7,8])
# newarr2 = arr2.reshape(3,3)
# print(newarr2)
# Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):

print("--Returns Copy or View?--")
# Check if the returned array is a copy or a view:
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr3.reshape(2,4))

print("----Unknown Dimension---")

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr4 = arr.reshape(2, 2, -1)

print(newarr4)
# Note: We can not pass -1 to more than one dimension.
