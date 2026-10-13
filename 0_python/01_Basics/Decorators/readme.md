# Python Decorators
# Basic Decorator
Define the decorator first, then apply it with @decorator_name above the function.

# *args and **kwargs
Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.
