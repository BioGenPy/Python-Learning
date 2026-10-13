'''
Dictionary
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
Dictionaries are written with curly brackets, and have keys and values:
'''

from operator import itemgetter
from os import name
import re


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary Items
'''
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.'''

thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 }
print(f"Dictionary Items: {thisdict['brand']}")

'''
# Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

# Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(f"this is dictionary :{thisdict}" )

#  Dictionary Items - Data Types
print(type(thisdict))


# The dict() Constructor

thisdictcontract = dict(name = "john", age = 36, country = "India")

print(f"this is dictionary function :{thisdictcontract}")

# Python - Access Dictionary Items

    # Accessing Items by Get the value of the "model" key:
    # There is also a method called get() that will give you the same result:
access_Item_disct = {
      "brand": "Ford",
        "model": "Mustang",
        "year": 1964
}
x = access_Item_disct.get("year")
print(f"This is dictionary item accessing : {access_Item_disct}")

    # Get Keys The keys() method will return a list of all the keys in the dictionary.
print("...........Get Keys The keys() method will return a list of all the keys in the dictionary...........")
car = {
        
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
        
    }
y = car.keys()

print(y) # before the change

car["color"] = "white"

print(y)
    # get Values
car["year"] = 2026

print(car)

print("............Check if Key Exists........................")

chekc_if_exit_in_disct = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in chekc_if_exit_in_disct:
    print("yes , model is one the kys in the dictionary")

print("............Change Values........................")  

change_dictionary_value = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
change_dictionary_value ["brand"] = "tata"
print(change_dictionary_value)

print("............Update Dictionary........................")  

change_dictionary_value.update({"year": 2026})

print(change_dictionary_value)

print("............Python - Remove Dictionary Items........................")  

remove_dictionary_iten ={
    
      "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
remove_dictionary_iten.pop("year")
print(remove_dictionary_iten)

# The del keyword removes the item with the specified key name:

delete_dictionary_item ={
   "brand": "Ford",
  "model": "Mustang",
  "year": 1964
 }
del delete_dictionary_item

print("delete_dictionary_item")

# The clear() method empties the dictionary:
print("..........The clear() method empties the dictionary:..................")

clear_dictionary_item = {
      "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
clear_dictionary_item.clear()
print(clear_dictionary_item)


# Python - Loop Dictionaries
print(".............Python - Loop Dictionaries.................")

'''
Loop Through a Dictionary
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

'''
loopDictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for d in loopDictionary :
    print(loopDictionary[d])
    
#  can also use the values() method to return values of a dictionary:

for dct in loopDictionary.values():
    print(dct)
    
#  can use the keys() method to return the keys of a dictionary:

for ke in loopDictionary.keys():
    print(ke)
# Loop through both keys and values, by using the items() method:

for dt, dc in loopDictionary.items():
    print(dt,dc)
    
# Python - Copy Dictionaries
print("...............Python - Copy Dictionaries............")

# Make a copy of a dictionary with the copy() method:
copyDict= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
myCopyDict = copyDict.copy()
print(myCopyDict)

# Another way to make a copy is to use the built-in function dict().

myCopyDictionary = {
 "brand": "Ford",
  "model": "Mustang",
  "year": 1964  
}

mydictionFuncation = dict(myCopyDictionary)
print(mydictionFuncation)

print("...............Python - Nested Dictionaries............")
# Python - Nested Dictionaries
'''
Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.
'''

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Ratn Roy",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamilyList = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamilyList)

# Access Items in Nested Dictionaries
'''To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary: '''

print(myfamilyList["child1"],[name])

# Loop Through Nested Dictionaries  You can loop through a dictionary by using the items() method like this:

for p, obj in myfamilyList.items():
    print(p)
    
    for t in obj:
        print(t + ':', obj )

'''
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

'''

