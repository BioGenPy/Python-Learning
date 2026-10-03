'''
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the if keyword.
'''

# If statement:
print("......................If statement:.............................")
a = 33
b = 200

if b > a :
  print("B is greater than a ")

# Checking if a number is positive:

number = 15
if number > 0 :
  print("The numder is positive")

# Multiple Statements in If Block
age = 20
if age >= 18 :
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

# Using Variables in Conditions Using a boolean variable:
is_logged_in = True
#is_logged_in = False
if is_logged_in:
  print("Welcome back!")
  
else:
  print("Your are not logged in")
  
# Python Elif Statement  
'''The Elif Keyword
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True. 
In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".
'''
print("..................Python Elif Statement....................")      
  
c = 33
d = 35
if d > c:
  print("c is greater than d")
elif c == d:
   print("d and c are equal")
  
print("..................Multiple Elif Statements....................")  

import sys

while True:
    user_input = input("Enter your Score (or type 'exit' to quit): ").strip().lower()

    # The user explicitly chooses when to exit
    if user_input == 'exit' or user_input == 'q':
        print("Goodbye!")
        sys.exit()  # Closes the program

    try:
        # Convert input to a float
        score = float(user_input)
        
        # Convert to an integer if it's a whole number
        if score.is_integer():
            score = int(score)
            
        # --- GRADING LOGIC MOVED INSIDE THE LOOP ---
        if score >= 90:
            print("Grade: A\n")
        elif score >= 80:
            print("Grade: B\n")
        elif score >= 70:
            print("Grade: C\n")
        elif score >= 60:
            print("Grade: D\n")
        else:
            print("Grade: F\n")
        # -------------------------------------------

    except ValueError:
        print("Invalid input! Please enter a valid number or type 'exit'.\n")
