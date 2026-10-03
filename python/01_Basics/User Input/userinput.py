print("====================User Input =====================")
print("Enter Your Name")
# name = input()
# print(f"Hello {name}")

print("----------Add a message in front of the user input:----------")
# name = input("Enter Your Name : ")
# print(f"Hello {name}")
print("----------Multiple Inputs:----------")
# You can add as many inputs as you want, Python will stop executing at each of them, waiting for user input:
# name  = input("Enter your name : ")
# print(f"Hello {name}")
"""
favl1 = input("What is your favourite animal :")
favl2 = input("What is your favourite color :")
favl3 = input("What is your favourite number :")
print(f"Do you want a {favl2} {favl1} with {favl3} legs ?")
"""

import math
print("--------------Input Number : float-----------------")
""" 
x = input("Enter  a Number :")
# Find the square root of the number:
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")
"""


print("-------------Validate Input-------------")
print("-------------Keep asking until you get a number:-------------")
y = True
while y == True:
  x = input("Enter a Number :")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again")
print("Thank you !")

