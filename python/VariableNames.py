'''
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
'''

# --------Illegal variable names:
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''
# =========== Multi Words Variable Names

'''
** Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

** Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

** Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"

** Python Variables - Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

** One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

** Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

** Python Tuples
Tuple
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets*.
ExampleGet your own Python Server
Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

'''
