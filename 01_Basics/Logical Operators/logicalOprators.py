from operator import truediv

print(".........................Python: Operator.  | And | .............")
"""The and Operator
The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true."""

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are Ture ")

print(".........................Python: Operator.  | or | .............")
"""The or Operator
The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true."""

if a > b or a > c:
    print("At list one condition is True ")

print(".........................Python: Operator.  | not  | .............")
"""The not Operator
The not keyword is a logical operator, and is used to reverse the result of the conditional statement."""

p = 34
q = 35
if not p > q:
    print("p is not greater than q")

print(
    ".........................Python: Operator.  | Combining Multiple Operators | ............."
)
"""Combining Multiple Operators
You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or. 
Python evaluates :
1=>not
2=>and
3=>or
"""
age = 25
is_Student = True
has_Discount_Code = False

if (age < 18 or age > 65) and not is_Student or has_Discount_Code:
    print("Discount Applies ! ")
else:
    print("Discount Not Applies ? ")

print(
    ".........................Python: Operator. Using Parentheses for Clarity ............."
)

temperature = 25
is_raining = False
is_weekend = False

if (temperature > 20 and not is_raining) or is_weekend:
    print("Garate day for outdoor Activity !")
else:
    print("Today is not for outdoor Activiy !")

print(
    "...............Python: Operator. Using Parentheses for Clarity  Examle 1............."
)
username = "admin"
password = "123@admin"
is_active = True


if username and password and is_active:
    print("loging Successful")
else:
    print("loging fail !")

print("...............Python: Operator. Python Nested If.............")
"""Nested If Statements
You can have if statements inside if statements. This is called nested if statements."""

x = 41

if x > 10:
    print("Above ten ! ")
if x > 20:
    print(" and also above ")
else:
    print("But not above 20")

print("this spidder")
