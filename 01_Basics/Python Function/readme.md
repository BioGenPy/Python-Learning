# Python Functions
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.

# Creating a Function
In Python, a function is defined using the def keyword, followed by a function name and parentheses:

# Calling a Function
To call a function, write its name followed by parentheses:
# Function Names
Function names follow the same rules as variable names in Python:
A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)

# Why Use Functions?
Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:

# Return Values
Functions can send data back to the code that called them using the return statement.
When a function reaches a return statement, it stops executing and sends the result back:

# The pass Statement
Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

# Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

# Parameters vs Arguments
The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the actual value that is sent to the function when it is called.

# Number of Arguments
By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with exactly 2 arguments.
# Default Parameter Values
You can assign default values to parameters. If the function is called without an argument, it uses the default value:

# Keyword Arguments
You can send arguments with the key = value syntax.

# Positional Arguments
When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:

# Mixing Positional and Keyword Arguments
You can mix positional and keyword arguments in a function call.
However, positional arguments must come before keyword arguments:

# Passing Different Data Types
You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
The data type will be preserved inside the function:

#  Return Values
Functions can return values using the return statement:

# Returning Different Data Types
Functions can return any data type, including lists, tuples, dictionaries, and more.

# Positional-Only Arguments
You can specify that a function can have ONLY positional arguments.
To specify positional-only arguments, add , / after the arguments:

# Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:
Without *,, you are allowed to use positional arguments even if the function expects keyword arguments:

# Combining Positional-Only and Keyword-Only
You can combine both argument types in the same function.
Arguments before / are positional-only, and arguments after * are keyword-only:

# *args and **kwargs
By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly:

# What is *args?
The *args parameter allows a function to accept any number of positional arguments.
Inside the function, args becomes a tuple containing all the passed arguments:

# Using *args with Regular Arguments
You can combine regular parameters with *args.
Regular parameters must come before *args:

# Practical Example with *args
*args is useful when you want to create flexible functions:

# Arbitrary Keyword Arguments - **kwargs
If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly:
Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentation.

# What is **kwargs?
The **kwargs parameter allows a function to accept any number of keyword arguments.
Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

# Using **kwargs with Regular Arguments
You can combine regular parameters with **kwargs.
Regular parameters must come before **kwargs:

# Combining *args and **kwargs
You can use both *args and **kwargs in the same function.
The order must be:
regular parameters
*args
**kwargs

# Unpacking Arguments
The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
Unpacking Lists with *
If you have values stored in a list, you can use * to unpack them into individual arguments:

# Unpacking Dictionaries with **
If you have keyword arguments stored in a dictionary, you can use ** to unpack them:
Remember: Use * and ** in function definitions to collect arguments, and use them in function calls to unpack arguments.

# Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# Function Inside Function
As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

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

# Basic Decorator
Define the decorator first, then apply it with @decorator_name above the function.
Decorators let you add extra behavior to a function, without changing the function's code.
A decorator is a function that takes another function as input and returns a new function.
By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
The function changecase is the decorator.
The function myfunction is the function that gets decorated.

# Multiple Decorator Calls
A decorator can be called multiple times. Just place the decorator above the function you want to decorate.

# Arguments in the Decorated Function
Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function:

# *args and **kwargs
Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.

# Decorator With Arguments
Decorators can accept their own arguments by adding another wrapper level.

# Multiple Decorators
You can use multiple decorators on one function.

This is done by placing the decorator calls on top of each other.

Decorators are called in the reverse order, starting with the one closest to the function.

# Preserving Function Metadata
Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

# Lambda Functions
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

# Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# Lambda with Built-in Functions
Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
Using Lambda with map()
The map() function applies a function to every item in an iterable:

# Using Lambda with filter()
The filter() function creates a list of items for which a function returns True:

# Using Lambda with sorted()
The sorted() function can use a lambda as a key for custom sorting:

# Recursion
Recursion is when a function calls itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# Base Case and Recursive Case
Every recursive function must have two parts:
A base case - A condition that stops the recursion
A recursive case - The function calling itself with a modified argument
Without a base case, the function would call itself forever, causing a stack overflow error.

# Fibonacci Sequence
The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. The sequence starts with 0 and 1:
0, 1, 1, 2, 3, 5, 8, 13, ...
The sequence continues indefinitely, with each number being the sum of the two preceding ones.
We can use recursion to find a specific number in the sequence:

# Recursion with Lists
Recursion can be used to process lists by handling one element at a time:

# Recursion Depth Limit
Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.
# Generators
Generators are functions that can pause and resume their execution.
When a generator function is called, it returns a generator object, which is an iterator.
The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
# The yield Keyword
The yield keyword is what makes a function a generator.
When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.

# Generators Saves Memory
Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.
For large datasets, generators save memory:

# Using next() with Generators
You can manually iterate through a generator using the next() function:

# Generator Expressions
Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets:

# Fibonacci Sequence Generator
Generators can be used to create the Fibonacci sequence.
It can continue generating values indefinitely, without running out of memory:

# Generator Methods
Generators have special methods for advanced control:
send() Method
The send() method allows you to send a value to the generator:
# close() Method
The close() method stops the generator: