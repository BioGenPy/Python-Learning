'''
Tuple
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets*.
'''


mytuple = ("apple", "banana", "cherry")
print(mytuple)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Items - Data Types
tuple = ("apple", "banana", "cherry")
tuple1 = (1,2,3,4,5)
tuple3 = (True, False, False)
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

'''
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''