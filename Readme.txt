# ===================== Step 3: Install VS Code Extensions
  Required
    Python (Microsoft)
    Pylance (Microsoft)
    Jupyter (Microsoft)
  Recommended
    Black Formatter
    isort
    Python Debugger
    Error Lens
    GitLens
    Better Comments
    Rainbow CSV
# ================================ Step 4: Create a Workspace 
    Python-Learning/
    │
    ├── Day01/
    ├── Day02/
    ├── Projects/
    ├── datasets/
    ├── notes/
    └── venv/
# ====================== Step 7: Activate Virtual Environment
   * Windows PowerShell
      .\venv\Scripts\Activate.ps1
   * Command Prompt
        venv\Scripts\activate
# ================= Step 8: Upgrade pip
    python -m pip install --upgrade pip
      Check:
           pip --version
# ================= Step 9: Install Required Packages
    pip install pandas
   * Install additional libraries you'll likely use:
        pip install numpy matplotlib openpyxl xlrd jupyter
    * For data analysis, I also recommend:
      pip install seaborn scikit-learn
# =============== Step 10: Verify Installation
      * Run
        python
      * then 
        import pandas as pd
          import numpy as np

          print(pd.__version__)
          print(np.__version__)
        Exit:
          exit()
# ================ Step 11: Select Python Interpreter
    Ctrl + Shift + P
    Type:
          Python: Select Interpreter
    Choose:
          venv
# ================ Step 12: Create Your First Python File
    Create:
        hello.py
      print("Hello Python")
      Run:
          python hello.py
# ===================== Step 13: Create Your First Pandas Program
    import pandas as pd

          students = {
              "Name": ["Kamal", "Rahul", "Amit"],
              "Age": [25, 30, 28],
              "City": ["Kolkata", "Delhi", "Mumbai"]
          }

          df = pd.DataFrame(students)

          print(df)

      * Run:
          python pandas_test.py
# ======================== Step 14: Install Jupyter Support
    Create:
      practice.ipynb
    or click:
        New File → Jupyter Notebook
    Example:
            import pandas as pd

              df = pd.DataFrame({
                  "Name": ["A", "B", "C"],
                  "Marks": [80, 90, 85]
              })

              df
# ======================= Step 15: Recommended Learning Folder Structure
                  Python-Learning
              │
              ├── 01_Basics
              │   ├── variables.py
              │   ├── operators.py
              │   ├── loops.py
              │   └── functions.py
              │
              ├── 02_OOP
              │
              ├── 03_FileHandling
              │
              ├── 04_Exception
              │
              ├── 05_Pandas
              │   ├── dataframe.py
              │   ├── filtering.py
              │   ├── sorting.py
              │   ├── merge.py
              │   ├── groupby.py
              │   └── excel.py
              │
              ├── datasets
              │
              ├── projects
              │
              └── venv
# ==================== Daily Practice Plan (30 Days)
    Week 1: Python fundamentals (variables, data types, loops, functions, collections).
    Week 2: OOP, file handling, exceptions, modules.
    Week 3: NumPy and Pandas (DataFrame creation, filtering, sorting, grouping, merging, missing data).
    Week 4: Real-world datasets, mini-projects, SQL basics, and interview questions.

    Since you mentioned you're learning Python and Pandas for a job, I recommend we follow a structured roadmap. Each day I'll give you:

    One focused topic.
    Hands-on coding exercises.
    An interview question.
    A small assignment.
    A mini project every weekend.

    By the end of 30 days, you'll have both interview preparation and a portfolio of practical exercises.

# ======================================= Week 1 – Python Fundamentals (Day 1)

   Today's topics:

    Variables
    Data Types
    User Input
    Type Conversion
    Practice Questions

        1. What is a Variable?
            A variable is a named location in memory used to store data.
            name = "Kamal"
            age = 36
            salary = 45000

            print(name)
            print(age)
            print(salary)
            --
      ✅ Variable Naming Rules

          ✅ Correct
          name = "Kamal"
          student_name = "Rahul"
          age1 = 20
          _myvariable = 100
          ❌ Wrong
          1name = "ABC"     # Cannot start with a number
          student-name = "" # Hyphen is not allowed
          class = "ABC"     # Reserved keyword
# Q: What is an exception?

Answer:

An exception is an error that occurs while a program is running. If it isn't handled, the program stops. Python provides try, except, else, and finally to handle exceptions gracefully.

# ------------Tomorrow: Day 2

We'll cover:

Comparison operators (==, !=, >, <, >=, <=)
Logical operators (and, or, not)
Type conversion (int, float, str, bool)
Assignment operators (+=, -=, *=, /=)
Membership operators (in, not in)
Identity operators (is, is not)
15–20 interview questions
10 coding exercises
1 mini project
# ------ Q: Why do we use while True with try/except?
Answer:

while True keeps asking the user until valid input is received.
try executes code that might fail.
except catches the error and prevents the program from crashing.
break exits the loop once the input is valid.

This pattern is widely used in command-line applications and is something interviewers like to see because it demonstrates robust input validation.
# -------- Why did you use while True instead of if?

A strong answer would be:

"if checks the condition only once. If the user enters invalid input, the program continues or exits. while True keeps asking until valid input is received, making the program more robust and user-friendly."

Interview Perspective

If an interviewer asks:

"Explain your calculator program."

A good answer:

"I created a reusable input validation function using exception handling. It accepts field names dynamically, validates integer input, and prevents the application from crashing. The calculator validates operators and handles division-by-zero errors."

That answer shows you understand the design, not just the syntax.
# ============== Next: Day 2 — Python Functions Deep Dive

You will learn:

Function parameters
Return values
Local vs global variables
Default arguments
*args and **kwargs
Lambda functions
Function-based mini project

# git 
git remote add origin https://github.com/.../Python-Learning.git
Step 9: Push Code
git branch -M main
git push -u origin main

#= Future Daily Workflow

Every day after practice:

git add .
git commit -m "Day 2 Python functions practice"
git push

# ========================================= Day 2 – Python Operators & Type Conversion (Today's Lesson)
        Topics :
                Comparison Operators
                Logical Operators
                Type Conversion
                Assignment Operators
                Membership Operators
                Identity Operators
                Interview Questions
                Coding Exercises
                Mini Project
        ---------------------------------------------------------       
        | Operator | Meaning               | Example  | Result  |
        | -------- | --------------------- | -------- | ------- |
        | `==`     | Equal                 | `5 == 5` | `True`  |
        | `!=`     | Not Equal             | `5 != 4` | `True`  |
        | `>`      | Greater Than          | `10 > 5` | `True`  |
        | `<`      | Less Than             | `2 < 1`  | `False` |
        | `>=`     | Greater Than or Equal | `5 >= 5` | `True`  |
        | `<=`     | Less Than or Equal    | `3 <= 2` | `False` |
# ------------------ Interview Question 1

Q: What is the difference between = and ==?
Answer:
= is the assignment operator. It assigns a value to a variable.
x = 10
== is the comparison operator. It checks whether two values are equal.
x == 10
returns True or False.
#-------------------Interview Question 2
Predict the output:
x = 10
y = 10
print(x == y)
Answer:
True
Because both values are equal.
********************Today's Assignment
Complete these three exercises without looking at the answers.
Exercise 1
Take two numbers from the user and print:
==
!=
>
<
>=
<=
# ============ Interview Question

Q: Why use elif instead of multiple if statements?

Answer:

if checks every condition.
elif stops checking once one condition is true.
elif is more efficient and makes it clear that only one branch should execute.

# ==========Next Topic

We'll continue with Logical Operators:

and
or
not

These operators are used constantly in interviews and real applications, especially when validating user input and writing business rules.


# ================================= Logical Operators

1. and Operator
Rule

Returns True only if all conditions are true.

Syntax
condition1 and condition2
Example 1
age = 25
salary = 50000

print(age >= 18 and salary >= 30000)

Output

True

Because:

25 >= 18  → True
50000 >= 30000 → True

True and True → True
Example 2
age = 16
salary = 50000

print(age >= 18 and salary >= 30000)

Output

False

Because:

16 >= 18 → False
50000 >= 30000 → True

False and True → False
Truth Table
A	B	A and B
True	True	True
True	False	False
False	True	False
False	False	False
Practice 1

Write a program that asks for:

Age
Salary

If:

Age ≥ 18
Salary ≥ 30000

Print

Eligible

otherwise

Not Eligible
2. or Operator
Rule

Returns True if at least one condition is true.

Example
marks = 80
sports = True

print(marks >= 90 or sports)

Output

True

Why?

marks >= 90 → False
sports → True

False or True → True
Truth Table
A	B	A or B
True	True	True
True	False	True
False	True	True
False	False	False
Practice 2

A student gets a scholarship if:

Marks ≥ 90
OR
Sports quota = Yes

Ask the user:

Enter Marks:
Sports Quota (yes/no):

Print

Scholarship Approved

or

Scholarship Rejected
3. not Operator

not reverses a Boolean value.

Example
logged_in = False

print(not logged_in)

Output

True

Because

not False = True

Another example

logged_in = True

print(not logged_in)

Output

False
Practice 3
is_admin = False

print(not is_admin)

Predict the output before running it.

Combining Operators

Real programs combine them.

Example:

age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible to Vote")
else:
    print("Not Eligible")
Interview Questions
Q1

What is the difference between and and or?

Answer
and requires every condition to be true.
or requires at least one condition to be true.
Q2

Predict the output.

print(True and False)

Answer

False
Q3

Predict the output.

print(True or False)

Answer

True
Q4

Predict the output.

print(not True)

Answer

False
Mini Project

Create a login checker.

Requirements:

Ask the user:

Username:
Password:

Valid credentials:

Username = admin
Password = python123

Use the and operator.

If both are correct:

Login Successful

Otherwise:

Invalid Username or Password
Assignment (Write the Code Yourself)

Complete these four programs:

Exercise 1

Eligibility checker using and.

Exercise 2

Scholarship checker using or.

Exercise 3

Experiment with not and predict the output before running.

Exercise 4

Login system using and.

Challenge Question

Without running the code, predict the output:

x = 10

print(x > 5 and x < 20)
print(x > 15 or x == 10)
print(not (x == 10))

Write your predictions first, then run the program to verify them.

Once you've completed the four exercises, paste your code here. I'll review it like an interviewer, point out any logic issues, and show you how to make it cleaner and more Pythonic.

# ------------- Interview Question
Q: What is this called?
print("Eligible" if condition else "Not Eligible")

Answer:

It is called the conditional expression or ternary operator.


def check_eligibility(age, salary)

# ===========
Next Assignment

Let's move to the or operator.

Build a Scholarship Eligibility Checker.

Requirements:

Ask for marks (integer).
Ask:
Sports Quota (yes/no):

Rules:

If marks ≥ 90 OR sports quota is "yes", print:
Scholarship Approved

Otherwise print:

Scholarship Rejected

# ---------------------------------------------
and → Both conditions must be true.
or → At least one condition must be true.
# ----------------------------------------------

#-------------------Interview Question
Q: Why did you use .strip().lower()?

A good answer:

.strip() removes leading and trailing whitespace. .lower() converts the input to lowercase, allowing inputs like "YES", "Yes", and "yes" to be treated the same. This makes user input handling more robust.

#-------------------------Next Lesson

We'll continue with the not operator. It's a short topic, but it's frequently used in authentication, permissions, feature flags, and validation logic. After that, we'll move on to assignment operators, membership operators, and identity operators to complete the operator section. Keep this pace, and you'll build a strong Python foundation.
#---------------- Week 1 – Day 2 (Part 3)
not Operator
What is not?

The not operator reverses a Boolean value.

Original	not Result
True	False
False	True

Think of it as "opposite of".

Example 1
is_logged_in = True

print(not is_logged_in)

Output

False

Explanation

is_logged_in = True

not True = False
Example 2
is_logged_in = False

print(not is_logged_in)

Output

True
Example 3
age = 15

print(not(age >= 18))

Output

True

Why?

age >= 18

15 >= 18

False

not False

True
Real Interview Example

Suppose you're building a website.

is_logged_in = False

if not is_logged_in:
    print("Please Login")

Output

Please Login

If

is_logged_in = True

nothing is printed.

This pattern is extremely common.

Practice 1

Predict the output before running.

is_admin = False

print(not is_admin)

Answer

True
Practice 2
has_license = True

if not has_license:
    print("Cannot Drive")
else:
    print("Can Drive")

Output

Can Drive
Practice 3
password = "python123"

entered_password = input("Password: ")

if not entered_password == password:
    print("Wrong Password")
else:
    print("Welcome")
Better Style

Instead of

if not entered_password == password:

write

if entered_password != password:

Both work, but != is clearer.

Interview Question 1

What is the output?

print(not True)

Answer

False
Interview Question 2
print(not False)

Answer

True
Interview Question 3

Predict the output.

x = 10

print(not(x > 5))

Answer

False

Because

x > 5

True

not True

False
Interview Question 4
is_active = False

if not is_active:
    print("Inactive")

Output

Inactive
Common Mistake

Many beginners write:

if not x == 10:

This is valid Python, but most developers prefer:

if x != 10:

Why?

Because it's easier to read.

Use not when you're negating a Boolean variable:

if not is_logged_in:

Use != when comparing values:

if password != entered_password:
Mini Project
Login Permission Checker

Requirements:

Ask the user:
Are you logged in? (yes/no):
Convert the input to lowercase.
Convert it into a Boolean variable:
is_logged_in = login_status == "yes"
Use not.

If the user is not logged in:

Please login first.

Otherwise:

Welcome to Dashboard.
Example

Input

Are you logged in? (yes/no): yes

Output

Welcome to Dashboard.

Input

Are you logged in? (yes/no): no

Output

Please login first.
Challenge (Interview Level)

Without running the code, predict the output:

is_admin = False
is_verified = True

print(not is_admin and is_verified)
Think step by step:
not False = ?

? and True = ?

Write down your prediction before running the program.

Assignment

Write two programs:

Program 1

A login checker using the not operator.

Program 2

A website access checker.

Rules:

Ask if the user has a subscription (yes/no).
Convert the answer into a Boolean.
If the user does not have a subscription, print:
Access Denied

Otherwise print:

Access Granted
Today's Interview Tip

When an interviewer asks:

"When should you use not instead of !=?"

A strong answer is:

Use not to negate a Boolean expression or Boolean variable (e.g., if not is_logged_in:).
Use != when checking whether two values are different (e.g., if password != entered_password:).

# -------------------- Mini Project
Login Permission Checker
Requirements:
Ask the user:
Are you logged in? (yes/no):
Convert the input to lowercase.
Convert it into a Boolean variable:
is_logged_in = login_status == "yes"
Use not.
If the user is not logged in:
Please login first.
Otherwise:
Welcome to Dashboard.
# ================= Interview Question

Q: What does this line do?

is_logged_in = is_logged_in_input == "yes"

Answer:

It compares the user's input with "yes".

If the input is "yes", is_logged_in becomes True.

If the input is "no", is_logged_in becomes False.

This is a concise way to convert user input into a Boolean value.

# ========================
Next Lesson

We'll move to Assignment Operators, which are used constantly in loops, counters, accumulators, and data processing.

You'll learn:

Operator	Example	Meaning
+=	x += 5	x = x + 5
-=	x -= 2	x = x - 2
*=	x *= 3	x = x * 3
/=	x /= 2	x = x / 2
%=	x %= 2	Remainder assignment
**=	x **= 2	Power assignment
//=	x //= 2	Floor division assignment

These operators appear frequently in coding interviews and real-world Python programs, especially when processing data and working with loops.


#===============1. += (Addition Assignment)
Normal Way
x = 10

x = x + 5

print(x)

Output

15
Short Way
x = 10

x += 5

print(x)

Output

15
Dry Run
x = 10

Memory

x = 10

Now

x += 5

becomes

x = x + 5
x = 15
2. -=
salary = 50000

salary -= 5000

print(salary)

Output

45000

Equivalent to

salary = salary - 5000
3. *=
quantity = 5

quantity *= 4

print(quantity)

Output

20

Equivalent

quantity = quantity * 4
4. /=
price = 200

price /= 4

print(price)

Output

50.0

Notice the result is a float.

5. %=
number = 17

number %= 5

print(number)

Output

2

Because

17 ÷ 5

Quotient = 3
Remainder = 2
6. **=
x = 4

x **= 2

print(x)

Output

16

Equivalent

x = x ** 2
7. //=
x = 17

x //= 3

print(x)

Output

5

Because

17 // 3 = 5
Summary Table
Operator	Equivalent
+=	x = x + value
-=	x = x - value
*=	x = x * value
/=	x = x / value
%=	x = x % value
**=	x = x ** value
//=	x = x // value

# ---Mini Project
Bank Balance Simulator

Start with:

balance = 10000

Then perform these operations:

Deposit ₹5000
+=
Withdraw ₹2500
-=
Add 5% interest

(Hint: interest is balance * 0.05)

Print the final balance.

# ------------- Tomorrow's Plan (Day 3)

We'll continue with topics that are heavily used in interviews and in pandas:

Membership Operators (in, not in)
Identity Operators (is, is not)
Strings (30+ interview questions)
Lists (50+ interview questions)
Tuples
Sets
Dictionaries (advanced)

Then we'll move into:

File Handling
Exception Handling
Object-Oriented Programming (OOP)
NumPy
Pandas
Real interview datasets
Data cleaning
Data analysis
Excel automation

The goal is to build the skills expected for a Python/Pandas job.

Have a good evening, and I'll see you tomorrow for Day 3. 👋

#============================= Day 3 – Operators & Strings ==================================
Part 1: Membership Operators
in
not in
Strings
Lists
Tuples
Dictionaries
10 interview questions
10 coding exercises
Part 2: Identity Operators
is
is not
None
Mutable vs Immutable
Interview pitfalls
10 interview questions
Part 3: Strings (Beginner)

Topics:

Indexing
Slicing
String methods
split()
join()
replace()
find()
count()
startswith()
endswith()
Formatting (f"", .format())

Practice:

15 coding exercises
20 interview questions

Mini Project:

Password Validator
Day 4 – Strings (Advanced)
Palindrome
Reverse String
Character Frequency
Anagram
Remove Duplicates
Word Counter
Email Validator
Interview Questions
Mini Project
Day 5 – Lists

Topics:

Create Lists
Access
Update
Delete
Loop
Nested Lists
List Methods
List Comprehension

Practice:

20 exercises

Mini Project:

Student Management System
Day 6 – Tuples & Sets
Tuples
Packing
Unpacking
Immutability
Interview Questions
Sets
Union
Intersection
Difference
Symmetric Difference

Mini Project:

Duplicate Finder
Day 7 – Dictionaries

Topics:

CRUD Operations
Nested Dictionaries
Looping
get()
items()
keys()
values()

Mini Project:

Employee Database

# ================== Part 1: Membership Operators

There are only two membership operators in Python:

Operator	Meaning
in	Checks if a value exists
not in	Checks if a value does not exist

They always return a Boolean:

True
False
1. Membership with Strings
Example 1
name = "Kamal"

print("K" in name)

Output

True

Because "K" exists in "Kamal".

Example 2
name = "Kamal"

print("z" in name)

Output

False
Example 3
name = "Python"

print("thon" in name)

Output

True

Python checks for substrings too.

Example 4
name = "Python"

print("java" not in name)

Output

True
2. Membership with Lists
languages = ["Python", "Java", "C#", "Go"]

print("Python" in languages)

Output

True
print("PHP" in languages)

Output

False
print("PHP" not in languages)

Output

True
3. Membership with Tuples
numbers = (10, 20, 30, 40)

print(20 in numbers)

Output

True
print(50 not in numbers)

Output

True
4. Membership with Dictionaries

This is a common interview question.

student = {
    "name": "Kamal",
    "age": 36,
    "city": "Kolkata"
}

print("name" in student)

Output

True
Why?

Because in checks keys, not values.

print("Kamal" in student)

Output

False

To check values:

print("Kamal" in student.values())

Output

True

To check keys:

print("city" in student.keys())

Output

True
Real Job Example
VALID_ROLES = ("admin", "teacher", "student")

role = input("Enter role: ").strip().lower()

if role in VALID_ROLES:
    print("Access Granted")
else:
    print("Invalid Role")

This pattern is used in authentication systems.

Interview Questions
1.
print("a" in "apple")

Answer: True

2.
print("A" in "apple")

Answer: False

Python is case-sensitive.

3.
numbers = [10, 20, 30]

print(40 in numbers)

Answer: False

4.
numbers = [10, 20, 30]

print(40 not in numbers)

Answer: True

5.
student = {"name": "Kamal"}

print("name" in student)

Answer: True

6.
student = {"name": "Kamal"}

print("Kamal" in student)

Answer: False

7.

How do you check dictionary values?

Answer:

"Kamal" in student.values()
8.

How do you check dictionary keys?

Answer:

"name" in student

or

"name" in student.keys()
9.

Which data types support membership operators?

Answer:

Strings
Lists
Tuples
Dictionaries
Sets
10.

What is the return type of in?

Answer:

bool
Coding Exercises
Exercise 1

Ask the user for a letter.

Check whether it exists in:

word = "python"
Exercise 2

Ask the user for a fruit.

Check if it exists in:

fruits = ["apple", "banana", "mango"]
Exercise 3

Ask the user for a country.

If it is not in:

countries = ("India", "USA", "Japan")

Print:

Country not supported
Exercise 4

Create:

student = {
    "name": "Kamal",
    "age": 36,
    "city": "Kolkata"
}

Ask the user for a key.

Print:

Key Found

or

Key Not Found
Exercise 5

Ask the user for a value.

Check if it exists in:

student.values()
Exercise 6

Create a list of programming languages.

Ask the user to enter one.

Tell them whether it is supported.

Exercise 7

Password Validator

Allowed passwords:

allowed_passwords = [
    "python123",
    "admin123",
    "welcome123"
]

Ask the user for a password.

If it exists:

Login Successful

Else:

Invalid Password
Exercise 8

Movie Search

movies = [
    "Inception",
    "Interstellar",
    "Avatar",
    "Titanic"
]

Search for a movie.

Exercise 9

Create a menu.

Allowed options:

("deposit", "withdraw", "balance", "exit")

Validate the user's input.

Exercise 10 (Interview Level)

Create a dictionary:

employees = {
    101: "Alice",
    102: "Bob",
    103: "Charlie"
}

Ask the user for an employee ID.

Tell them whether the ID exists.

Mini Project
User Registration Validator

Requirements:

Allowed usernames:
existing_users = [
    "kamal",
    "admin",
    "guest"
]
Ask for a new username.
If the username already exists:
Username already taken.

Otherwise:

Username available.
Your Assignment

Complete these in order:

✅ Exercise 1–5
✅ Exercise 6–10
✅ Mini Project

# ================== Which data types support membership operators?

Answer:

Strings
Lists
Tuples
Dictionaries
Sets
# ========= 10.

What is the return type of in?
ANS : bool

# ---------------------- Exercise 1
Ask the user for a letter.
Check whether it exists in:


#------------------Next Lesson
We'll cover Identity Operators (is, is not).
This topic is short but very important because interviewers frequently ask questions like:
x = None
if x is None:
    ...
or
a = [1, 2]
b = a
print(a is b)
print(a == b)
Understanding the difference between is and == is a common interview question, and it's essential before moving on to object-oriented programming and pandas.

# =========================================== Week 1 – Day 3 (Part 2)


Week 1 – Day 3 (Part 2)
Identity Operators

There are only two identity operators.

Operator	Meaning
is	Are both variables the same object in memory?
is not	Are they different objects in memory?

They return:

True
False
First Understand ==

== compares values.

Example:

a = 10
b = 10

print(a == b)

Output

True

Because

10 == 10
Now is

is compares identity (memory object).

Example

a = 10
b = 10

print(a is b)

Output

True

Looks the same...

But wait...

Example 2
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)

Output

True

Because both lists contain the same values.

Now

print(a is b)

Output

False

Why?

Because Python created two different list objects.

Imagine memory like this:

Memory

a ----> [1,2,3]

b ----> [1,2,3]

Same values

Different locations.

Example 3
a = [1, 2, 3]

b = a

print(a == b)

print(a is b)

Output

True
True

Why?

Because

Memory

a ----\
       > [1,2,3]
b ----/

Both variables point to the same object.

Example 4

Change one list.

a = [1, 2, 3]

b = a

b.append(4)

print(a)

Output

[1,2,3,4]

Many beginners expect:

[1,2,3]

Wrong.

Both variables refer to the same list.

Example 5
a = [1,2]

b = [1,2]

b.append(3)

print(a)

Output

[1,2]

Because

a

and

b

are different objects.
None

This is where interviews become interesting.

user = None

Means

No value

Not

0

or

False

or

""

Correct way

if user is None:
    print("No User")

Never write

if user == None:

Python's style guide (PEP 8) recommends:

is None
is not

Example

user = "Kamal"

if user is not None:
    print("User Found")

Output

User Found
Interview Questions
Q1

Difference between

==

and

is

Answer

== compares values.

is compares object identity.
Q2

Predict

a = [1,2]

b = [1,2]

print(a == b)

Answer

True
Q3
a = [1,2]

b = [1,2]

print(a is b)

Answer

False
Q4
a = [1,2]

b = a

print(a is b)

Answer

True
Q5
x = None

print(x is None)

Answer

True
Q6
x = None

print(x == None)

Answer

True

But interviewers expect

x is None
Q7
x = None

print(x is not None)

Answer

False
Q8

What does

is not

mean?

Answer

Checks that two variables do NOT reference the same object.
Q9

Which is recommended?

if x is None:

or

if x == None:

Answer

is None
Q10

Why?

Answer

Because:

clearer
faster for identity checks
follows PEP 8
standard Python practice
Practice Exercises
Exercise 1
a = 100

b = 100

print(a == b)

print(a is b)

Predict before running.

Exercise 2
name1 = "Python"

name2 = "Python"

print(name1 is name2)
Exercise 3
list1 = [10,20]

list2 = [10,20]

print(list1 == list2)

print(list1 is list2)
Exercise 4
list1 = [10,20]

list2 = list1

print(list1 is list2)
Exercise 5

Create:

employee = None

Use

is None

to check.

Exercise 6

Ask the user for a name.

If they press Enter without typing anything:

name = None

Then check

is None
Exercise 7

Create:

a = []

b = a

Append

100

Print both.

Explain why both changed.

Exercise 8

Create

a = []

b = []

Append

100

only to b.

Print both.

Exercise 9

Write a function:

def check_employee(employee):

If

employee is None

return

Employee Not Found

Else

Employee Found
Exercise 10 (Interview Level)

Predict the output without running:

a = [1,2,3]

b = a

c = [1,2,3]

print(a == b)

print(a is b)

print(a == c)

print(a is c)
Mini Project
Employee Lookup

Requirements:

Create:
employee = None
Ask the user:
Enter employee name:
If the user enters nothing:
employee = None

Otherwise

employee = input(...)
Use:
is None

If no employee:

Employee Not Found

Otherwise:

Welcome Kamal
Interview Tip

If an interviewer asks:

"When should you use is instead of ==?"

A strong answer is:

Use == when comparing values, such as numbers, strings, or lists. Use is when checking object identity, especially for singleton objects like None. A common example is if value is None: because it follows Python's recommended style and checks identity rather than equality.

Your Assignment

Write the following yourself:

✅ Exercises 1–10
✅ Mini Project