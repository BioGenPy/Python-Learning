'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''

# add tuple in tuple
thistuple = ("apple", "banana", "cherry")
y = ("ornage",)
thistuple = thistuple + y
print(thistuple)
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

z = list(thistuple)
z.remove("ornage")
thistuple = thistuple (y)
print(thistuple)

tt = list(thistuple)
del thistuple
print(thistuple)

