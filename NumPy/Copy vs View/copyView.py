print("The Difference Between Copy and View")
print("-----COPY------")
import numpy as np 
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

print("----- VIEW: ------")

view_arr = np.array([1,2,3,4,5])
y = view_arr.view()
y[2] = 31
print(view_arr)
print(y)

print(
    "---Print the value of the base attribute to check if an array owns it's data or not:--"
)

arr_od = np.array([1,2,3,4,5])
p = arr_od.copy()
q = arr_od.view()

print(p.base)
print(q.base)