print("=====================Python String Formatting =========================")
print(".........F-Strings..........")
# To specify a string as an f-string, simply put an f in front of the string literal, like this:
txt = f"This price is 100 rupess"
print(txt)


print("==================== Placeholders and Modifiers =======================")
# To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.

price = 59
txt = f"The price is ₹{price}"
txt1 = f"The price is ₹{ price : .2f}"
txt2 = f"The price is ₹{100 : .2f}"
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
print(txt1, "\n", txt ,"\n", txt2)

print("============ Perform Operations in F-Strings =====================")
# You can do math operations:
f = f"The price is ₹:{ 20 * 50 }"
print(f)
print("..........Add taxes before displaying the price:...........")
price = 59
tax = 0.25
final_price = f"The price is ₹{price + (price * tax)}"

print(final_price)

print("..........perform if...else:...........")
price = 49
txt = f"It is very {"'Expensie' if price>50 else 'Cheap' "}"
print(txt)

print("..................Execute Functions in F-Strings.........")
# You can execute functions inside the placeholder:
# Use the string method upper()to convert a value into upper case letters:
fruit = "apple"
text = f"I love {fruit.upper()}"
print(text)

print(
    "====The function does not have to be a built-in Python method, you can create your own functions and use them:=="
)
# Create a function that converts feet into meters:
def myconvert(x):
  return x * 0.3048
txt = f"The plane is flying at a {myconvert(30000)} meter altitude "
print(txt)

print("================String format()===================")
price = 49
txt = "The price is ₹ {} "
print(txt.format(price))

print("...........Multiple Values...........")
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for  ₹{:.2f} ."

print(myorder.format(quantity, itemno, price))
print("...Index Numbers...")
myorder = "I want {0} pieces of item number {1} for ₹{2:.2f} ."
print(myorder.format(quantity, itemno, price))

print(".... if you want to refer to the same value more than once, use the index number:..."
)
age = 36
name = "Aditya Mridha"
txt = "His name  is {1}.  {1} is {0} years old. "
print(txt.format(age, name))

print("...........Named Indexes................")
"""You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):"""
myorder = " I have a {carname}, it is a {model}"
print(myorder.format(carname = "Ford", model = "Mustang"))
