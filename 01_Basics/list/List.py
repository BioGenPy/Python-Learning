mylist =[ "apple", "banana", "cherry" ]
print(mylist)

# create tuple
thistuple = ("apple", "banana", "cherry")
print("This tuple :",thistuple)

# another tuple
this_is_tuple = "apple", "banana", "cherry"
print("This is Tuple without parenthese",this_is_tuple)

# Tuple length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple with one Item
thistupel=("apple", "banana", "cherry")
print(thistupel)

# create empty typle
thisemptytuple = ()
print(thisemptytuple)

# tuple items data type
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = ("apple", "banana", "cherry")

#tuple constructor

thistupconstroctor = tuple(("apple", "banana", "cherry"     ))
print(thistupconstroctor)

# This example of retuns the items for cherery and to the end:
thistuple = ("apple", "banana", "cherry")
print(thistuple[2:])
print(thistuple[:2])

# update tuple x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
print(y)

# add items
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)