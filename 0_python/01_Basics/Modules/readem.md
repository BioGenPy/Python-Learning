# What is a Module?
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
# Note: When using a function from a module, use the syntax: module_name.function_name.
# Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
# Naming a Module
You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
You can create an alias when you import a module, by using the as keyword:
# Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.

# Using the dir() Function
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# Import From Module
You can choose to import only parts from a module, by using the from keyword.
Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]