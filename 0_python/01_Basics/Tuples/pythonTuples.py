from turtle import ontimer


print("1.....................Python Tuples.....................")


mytuple = ("apple", "banana","cherry")

print(f"The length is mytuple: {len(mytuple)}") 
print(mytuple)

#  ....................Tuples can also be created without the parentheses:

thistuple = "book","pen","colorbox","pencle box"
print(f"The length is thistuple: : {len(thistuple)}")
print(thistuple)


'''Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc. '''

#1............................... Create Tuple With One Item
'''To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.'''
   # One item tuple, remember the comma:
print("2.....................Create Tuple With One Item.....................")
oneTuple = ("Python",)
print(f"Type of : {type(oneTuple)} | Value: {oneTuple}")

# 2 ......................To create an empty tuple, use round brackets with no content.
print("3.....................Create an Empty Tuple.....................")

emptyTuple = ()
print(f"This is  an empty tuple : {type(emptyTuple)} ")
# 3 ................ Tuple Items - Data Types
print("4.....................Tuple Items - Data Types.....................")
# String, int and boolean data types:

tupleItemsdataTypes = (
    ("apple", "banana", "cherry"),
    (10, 20, 30, 40, 50),
    (True, False, False)
                    )
# Print a table header
print(f"{'Data Type':<12} | {'Tuple Content'}")
print("-" * 70)
# print(f"Tuple Items - Data Types :  {type(tupleItemsdataTypes )}  \n Tuples are : {tupleItemsdataTypes}")

# Loop and print each row formatted nicely
for sub_tuple in tupleItemsdataTypes :
  data_type = type(sub_tuple[0]).__name__
  print(f"{data_type : <12}   {sub_tuple}")

# -------- A tuple with strings, integers and boolean values:
# From Python's perspective, tuples are defined as objects with the data type 'tuple':

print("5.....................The tuple() Constructor.....................")
tupleMethod = tuple(("apple", "banana", "cherry")) # # note the double round-brackets
print(tupleMethod)

print("6.....................Python - Access Tuple Items.....................")
# You can access tuple items by referring to the index number, inside square brackets:

accessTuple = tuple(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))

# 1. Loop through each item in the tuple
for subTupel_data in accessTuple:
    # Get the type name of the item itself (e.g., 'str')
    dataTypeTuple = type(subTupel_data).__name__
    
    # 2. Print the information inside the loop (removed single quotes around dataTypeTuple)
    print(f"Access Tuple Item data Type : {dataTypeTuple:<12} | Item: {subTupel_data}")

print(f"\nFull Tuple: {accessTuple}  ")
print(f"First Item: {accessTuple[0:7]}")


#  Check if Item Exists
''' To determine if a specified item is present in a tuple use the in keyword: '''
itemChechTuple = ("apple", "banana", "cherry")
if "apple" in itemChechTuple:
  print("Yes, 'apple' is in the fruits tuple")
else:
  print("No, 'apple' is in the fruits tuple")

# Python - Update Tuples
print("....................Python - Update Tuples......................")
''' Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple. '''

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"

x = tuple(y)
print(y)
 
print("....................Python - Add Items Tuples......................")
 
'''Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.'''

y.append("orange",)
x = tuple(y)
print(x)

'''2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:'''

add_multi_tuple = ("apple", "banana", "cherry")
g = ("gova",)
add_multi_tuple += g

print(add_multi_tuple)

print("....................Python - Remove Items Tuples......................")
'''Note: You cannot remove items in a tuple.
Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items: '''
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
removeTuple = ("apple", "banana", "cherry")
r = list(removeTuple)
r.remove("apple")
removeTuple = tuple(r)
print(removeTuple)
print("....................Python - delete Items Tuples......................")
# Or you can delete the tuple completely:
deleteTuple = ("apple", "banana", "cherry")
deleteTuple =()
print(deleteTuple)
print("....................Python - Unpack Tuples Tuples......................")

'''Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

'''
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
(f1,f2,f3) = fruits 
print(f1)
print(f2)
print(f3)
'''The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.'''

print("....................Python - Using Asterisk*......................")
'''If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:'''

astriskTuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
(a1,a2,*a3) = astriskTuple
print(a1)
print(a2)
print(a3)
print("....................Python - Loop Tuples......................")

# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

loopTuple = ("apple", "banana", "cherry")
for lt in loopTuple:
  print(lt)
print("....................Python - Index Numbers......................")
# Loop Through the Index Numbers

for i in range(len(loopTuple)):
  print(loopTuple[i])
print("....................Python - Using a While Loop......................")

'''You can loop through the tuple items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.

Remember to increase the index by 1 after each iteration.'''

whileLoopTuple = ("apple", "banana", "cherry")
i = 0
while i < len(whileLoopTuple):
  print(whileLoopTuple[i])
  i = i + 1
print("....................Python - Join Tuples......................")
'''Join Two Tuples
To join two or more tuples you can use the + operator:'''
tup1 = ("a", "b" , "c")
tup2 = (1,2,3,4)
tup3 = tup1 + tup2
print(tup3)
print("....................Python - Multiply Tuples......................")
'''Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:'''
multiTuple = ("apple", "banana", "cherry")
resultTuple = multiTuple * 2
print(resultTuple)

print("....................Python - Tuple Methods ......................")
'''Tuple Methods
Python has two built-in methods that you can use on tuples.
Method	Description
* count()	Returns the number of times a specified value occurs in a tuple
* index()	Searches the tuple for a specified value and returns the position of where it was found'''
