print(".................Python Conditions and If statements......................")

a = 30
b = 200
if b > a:
  print("B is the grater thean a ")
  
'''Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.'''

'''
Multiple Statements in If Block
'''
age = 20
if age >= 18:
  print("you are an adult ")
  print("Your can vote ")
  print("You have full legal rights")

# Using Variables in Conditions
# Boolean variables can be used directly in if statements without comparison operators.

is_logged_in = True
if is_logged_in:
  print("Welcome back!")
  
print(".........................Python Elif Statement.........................")
'''The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.'''

r = 37
s = 35
if r > s :
  print("R is greater than a ")
elif r == s:
  print(" R and S are equal")
else:
  print( "R and S are not equal ")

print(".........................Python : Multiple Elif Statements.........................")

'''How Elif Works
When you use elif, Python evaluates the conditions from top to bottom. As soon as it finds a condition that is true, it executes that block and skips all remaining conditions.
Important: Only the first true condition will be executed. Even if multiple conditions are true, Python stops after executing the first matching block.'''



#score = int(input(" Plz Enter Your Score : "))

score = 75

if score >= 90:
  print("Garade: A ")
elif score >= 80:
  print("Grade : B")
elif score >= 70:
  print("your Grade : c")
elif score >= 60:
  print("Grade : D")
  

print(".............When to Use Elif..............")
'''Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition. '''

day = 7

if day ==1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

print(".............Python Else Statement ..............")
'''The Else Keyword
The else keyword catches anything which isn't caught by the preceding conditions.
The else statement is executed when the if condition (and any elif conditions) evaluate to False.'''

p = 20 
q = 33

if p > q :
  print("P is greater than q ")
elif  p == q:
  print("P and q are equal ")
else:
  print(" p is greater than q ")

'''
How Else Works
The else statement provides a default action when none of the previous conditions are true. Think of it as a "catch-all" for any scenario not covered by your if and elif statements.
'''

'''
Note: The else statement must come last. You cannot have an elif after an else.
'''
number = 7 
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

print("..................Complete If-Elif-Else Chain...............")

temperature = 22

if temperature > 30 :
  print("It is hot outside !")
elif temperature >20:
  print("it's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

print("..................Python : Else as Fallback ...............")
'''
The else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.
'''
username = "Dipika"


if len(username) > 0:
  print(F" Welcome , {username} ! ")

else:
  print("Error : Username can not be empty ")
  

  




