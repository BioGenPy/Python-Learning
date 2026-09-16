# Python Functions
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.

# Creating a Function
In Python, a function is defined using the def keyword, followed by a function name and parentheses:

# Function Names
Function names follow the same rules as variable names in Python:
A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)

# Python Function Arguments
Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameters vs Arguments
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the actual value that is sent to the function when it is called.
# Number of Arguments
By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with exactly 2 arguments.

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

