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
# Fibonacci Sequence Generator
Generators can be used to create the Fibonacci sequence.
It can continue generating values indefinitely, without running out of memory:

# send() Method
The send() method allows you to send a value to the generator:Generators have special methods for advanced control: