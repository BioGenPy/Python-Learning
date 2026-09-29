print("============NoneType================")
x = None
print(type(x))

print("=================Comparing to None==========")
# To compare a value to None, use the identity operator is or is not
result = None
if result is None:
    print("No result yet")
else:
    print("Result is ready")

# Similar example, but using is not instead:
result1 = None
if result1 is not None:
    print ("Result is ready")
else:
    print("No result yet")
print("------True or False-----------")
# None evaluates to False in a boolean context.
# Check truthiness:
print(bool(None))

print("--------------Functions returning None--------------")
# Functions that do not explicitly return a value return None by default.
def myfunction():
  x = 5
  x = myfunction
print(x)
