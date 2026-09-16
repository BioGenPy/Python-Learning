from os import name


print("................Python : Dictionaries.....................")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print("................Python : Dictionary Items.....................")
'''Dictionary items are ordered, changeable, and do not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.'''

itemDisct = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f" This is Items list : {itemDisct['model']}")

print("................Python : Dictionary Length.....................")

lendict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print( f" This is Distionary list :  {len(lendict) } ")

print("................Python : Data Types.....................")
dataDictionay = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print( f" This is Distionary data Type :  {type(dataDictionay) } ")

print("................Python : The dict() Constructor.....................")
constractdictionary = dict(name = "jhaon", age = 34 , country = "india")
print(constractdictionary)

print("................Python : Access Dictionary Items.....................")
'''Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets:'''

accessDictItem = {
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = accessDictItem["brand"]
print(f" This is access Dictionary Items : {x}")

# There is also a method called get() that will give you the same result:

y = accessDictItem["model"]

print(f" This is get method to access dictionory Items : {y}")

# The keys() method will return a list of all the keys in the dictionary.

z = accessDictItem.keys()
print(f" This key method to asscess dictionary Items : {z}")

print("..........Add a new item to the original dictionary, and see that the keys list gets updated as well:")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

c = car.keys()
print(f" Before change dictionary items :{c}")

car["color"] = "white"

print(f"Print after change dictionary value : {car} | {c}")

print("................Python :Get Values..................  ")
# The values() method will return a list of all the values in the dictionary.
car = {
  "brand": "Ford",
"model": "Mustang",
"year": 1964
}
p = car.values()
print(f" Print benfore change  {p}") # before the change value
car["brand"] = 2026
print(f" print value useing python values method : {p}")
print("................Python :Add new Items..................  ")

addCaredict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

ac = addCaredict.values()

addCaredict["color"] = "Yellow"
print(f" Add Dictionary + addCaredict:  {ac}")

print(" ......................... Check if Key Exists .........................")
'''
To determine if a specified key is present in a dictionary use the in keyword:

'''
keyExit = {
  
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  
}

if "brand" in keyExit:
  print("Yes, 'brand' is one of the keys in the keyExit in the dictionary ")
else:
  print("No, 'brand' is one of the keys in the keyExit in the dictionary ")

print("..................Python - Change Dictionary Items.......................")
itemChangeDictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  
}
itemChangeDictionary['year'] = 2026
print(f" Change Dictionary Value :  {itemChangeDictionary}")


print("..................Python - Update Dictionary......................")

'''The update() method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs. '''

updateDictionary = {
  
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
updateDictionary.update({"year" : 2026})

print(f" Update Dictionary Value : {updateDictionary}")


print("..................Python - Remove Dictionary Items ......................")
print("..................Python - pop method......................")
removeDictionary = {
    "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f" Before  Remove Dictionary Items :  Total Items :  {len(removeDictionary)}   | {removeDictionary}  ")
removeDictionary.pop("brand")
print(f" After  Remove Dictionary Items :  Total Items :  {len(removeDictionary)}   | {removeDictionary} ")

print("..................Python - popitem method......................")
'''The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):'''
popItemDictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
popItemDictionary.popitem()
print(popItemDictionary)

print("..................Python - del method......................")
''' The del keyword removes the item with the specified key name: '''

delDictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del delDictionary["model"]
print(f" This is Del mothad to delete specified Item to Delete :  {delDictionary}" )

delDct = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del delDct 

print("..................Python - clear method......................")

'''The clear() method empties the dictionary:'''

emptyDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
emptyDict.clear()
print(emptyDict)


print(".........................Python - Loop Dictionaries............................")
# Print all key names in the dictionary, one by one:
loopDictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for loop in loopDictionary:
  print(loop)
# Print all values in the dictionary, one by one:
print("* Print all values in the dictionary : Values :- ............................")
for loopkey in loopDictionary.values():
  print(f"This is loop through key :  {loopDictionary}")
  
print("* Print all values in the dictionary: |loopDictionary:|  keys:- ............................")
for loopvalues in loopDictionary.keys():
  print(f"This is loop through Values :  {loopDictionary}")

print("* Print all values in the dictionary: |loopDictionary:|  Items:- ..............")

loopDictionaryItems = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i ,j in loopDictionaryItems.items():
  print(f" This is Disctionary Itmes : {i,j}")


print(".........................Python - Copy Dictionaries............................")
'''
Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().
'''
copyDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
myDcit = copyDict.copy()
print(f" This is copy Dictionary : {myDcit}")

print(".........................Python - Nested Dictionaries ............................")
'''Nested Dictionaries
A dictionary can contain dictionaries, this is called nested dictionaries.'''

myfamilyDict = {
  
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
print(myfamilyDict)

print(".........................Python - Access Items in Nested Dictionaries............................")

print(myfamilyDict["child3"] ["name"])

print(".....Python - Loop Through Nested Dictionaries.......")

for myd ,obj in myfamilyDict.items():
  print(myd)
  
  for mye in obj:
    print(mye + ':', obj[mye])