
print("..............A simple recursive function that counts down from 5:...........")
def countdown(n):
  if n <= 0:
    print("Done !")
  else:
    print(n)
    countdown(n-1)
countdown(5)

print("...........Base Case and Recursive Case.........")
# The base case is crucial. Always make sure your recursive function has a condition that will eventually be met.
def factorial(n):
  # Base function
  if n == 0 or n ==1:
    return 1
    # Recursive case
  else:
    return n * factorial(n-1)
print(factorial(5))

print("....................Fibonacci Sequence...................")
# Find the 7th number in the Fibonacci sequence:
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))    

print("....................Recursion with Lists...................")
# Recursion can be used to process lists by handling one element at a time:

# Calculate the sum of all elements in a list:

def sum_list(num):
  if len(num) == 0:
    return 0
  else:
    return num[0] + sum_list(num[1:])

my_list = [1,2,3,4,5]
print(sum_list(my_list))

print("........Find the maximum value in a list:..............")

def find_max(num):
  if len(num) == 1:
    return num[0]
  else:
    max_of_rest = find_max(num[1:])
    return num[0] if num[0] > max_of_rest else max_of_rest
  
my_list = [3,7,5,7,9,1,5]
print(find_max(my_list))

print("........Recursion Depth Limit.......")
# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


