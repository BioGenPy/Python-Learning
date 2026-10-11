print("--------------------NumPy Array Slicing----------------")
import numpy as np 
print(
    "---------Slice elements from index 1 to index 5 from the following array--------"
)
arr = np.array([1,2,3,4,5,6,7])
print(arr[0:5])
print("--Slice elements from index 4 to the end of the array---")


print(f"First  four element :", arr[:4])

print(f"Last  four element :", arr[4:])
print("---Use the minus operator to refer to an index from the end:")
print(arr[-3:-1])
print("---Use the step value to determine the step of the slicing:")
print(arr[0:7:2])
print("---Return every other element from the entire array:")
print(arr[::2])
print("-----Slicing 2-D Arrays----")
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr1[0, 1:4])
print("....From both elements, return index 2:")
print(arr1[0:2,2])
print(
    "...From both elements, slice index 1 to index 4 (not included), this will return a 2-D array::"
)
print(arr1[0:2,0:2])
