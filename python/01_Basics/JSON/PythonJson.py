import json

print("-----------Convert from JSON to Python::----------")
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

print("-----------Convert from Python to JSON:----------")
# a python object (dict)

j =  {"name": "John", "age": 30, "city": "Bongaon"}

# convert into JSON:

h = json.dumps(j)

print(h)

print(
    "-----------Convert Python objects into JSON strings, and print the values:----------"
    
)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("Convert a Python object containing all the legal data types")

po = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}
print("use indent=4)")
print(json.dumps(po, indent=4))
print( " You can also define the separators, ")
json.dumps(po, indent=4, separators=(". ", " = "))
print()
