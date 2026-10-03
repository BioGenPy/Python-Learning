# Scope
A variable is only available from inside the region it is created. This is called scope.
# Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.

# Naming Variables
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
# Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global. 

# Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.

# The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:
Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace
