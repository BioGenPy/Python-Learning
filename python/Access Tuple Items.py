thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# Range of Indexes
'''
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new tuple with the specified items.
'''

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# Check if Item Exists
#To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    # print(thistuple['apple'])
    print("yes",'apple' "is in the fruits tuple ")