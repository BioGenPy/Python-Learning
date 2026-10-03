# Python range
The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
This set of numbers has its own data type called range.
Note: Immutable means that it cannot be modified after it is created.
Creating ranges
The range() function can be called with 1, 2, or 3 arguments, using this syntax:
range(start, stop, step)
# Call range() With One Argument
If the range function is called with only one argument, the argument represents the stop value.
The start argument is optional, and if not provided, it defaults to 0.
range(10) returns a sequence of each number from 0 to 9. (The start argument, 0 is inclusive, and the stop argument, 10 is exclusive).
# Call range() With Two Arguments
If the range function is called with two arguments, the first argument represents the start value, and the second argument represents the stop value.
range(3, 10) returns a sequence of each number from 3 to 9:
# Call range() With Three Arguments
If the range function is called with three arguments, the third argument represents the step value.
The step value means the difference between each number in the sequence. It is optional, and if not provided, it defaults to 1.
range(3, 10, 2) returns a sequence of each number from 3 to 9, with a step of 2:

# Using ranges
Ranges are often used in for loops to iterate over a sequence of numbers.
# Using List to Display Ranges
The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.

Therefore, ranges are often converted to lists for display.

# Slicing Ranges
Like other sequences, ranges can be sliced to extract a subsequence.
Note: The first print statement returns the value at index 2, and the second print statement returns a new range object, from index 0 to 3.

# Membership Testing
Ranges support membership testing with the in operator.

