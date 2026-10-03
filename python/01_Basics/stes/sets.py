print ("...........................Python Sets..................")

myset = {"apple", "banana", "cherry"}
print(myset)

print ("...........................Python Duplicates Not Allowed .................")
# Sets cannot have two items with the same value. Duplicate values will be ignored:
thisSet = {"apple", "banana", "cherry", "apple"}
print(thisSet)

print ("...........................Python :The values True and 1 are considered the same value in sets, and are treated as duplicates .................")
duplicatSet = {"apple", "banana", "cherry", True, 1, 2}
print(duplicatSet)

print ("...........................Python :The values False and 0 are considered the same value in sets, and are treated as duplicates: .................")
# False and 0 is considered the same value:
falseSet = {"apple", "banana", "cherry", False, True, 0}
print(falseSet)

print ("...........................Python :Get the Length of a Set .................")

# To determine how many items a set has, use the len() function.
lenSet = {"apple", "banana", "cherry"}
print(len(lenSet))

print ("...........................Python :Set Items - Data Types .................")

# Set items can be of any data type: String, int and boolean data types:
setDataType = (
  {"apple", "banana", "cherry"},
  {1, 5, 7, 9, 3},
   {True, False, False}
)
print(type(setDataType))
print(setDataType)

print ("...........................Python :The set() Constructor.................")
# It is also possible to use the set() constructor to make a set.
# Using the set() constructor to make a set:
constracSet = set(("apple", "banana", "cherry"))
print(constracSet)

print ("##################Python :Access Set Items#######################")
'''Access Items
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.'''
print("............Loop through the set, and print the values:...........")
loopSet = {"apple", "banana", "cherry"}
for x in loopSet:
  print(x)
print("")