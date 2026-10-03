print(".................Built-in Math Functions:.min() and max()................")
print(".................Built-in Math Functions:......abs()...........")

x = min(5,5,6,7)
y = max(12,14,18,1)
print(f"Max value of list :  {y} ")
print(f"Min value of list :  {x} ")

print(".................Built-in Math Functions:......abs()...........")


ab = abs(-2.5)
print(f"absolute (positive) value of the specified number :  {ab} ")

print(".................Built-in Math Functions:......power()...........")

p = pow(2,3) # 8
print(f"Power value of list :  {p} ")

import math as mth
print(".................Math Module:......power() ...........")
m = mth.sqrt(64)
print(f"Squer root value of list :  {m} ")

print(".................Math Module:......ceil() , floor()...........")

c = mth.ceil(1.04)
d = mth.floor(1.04)
print(f"ceil()  method rounds a number upwards to its nearest integer:  {c} ")
print(f"floor() method rounds a number downwards to its nearest integer:  {d} ")


print(f"The math.pi constant, returns the value of PI (3.14...)")
pa = mth.pi

print(f"The math.pi constant, returns the value of PI (3.14...) :  {pa} ")
