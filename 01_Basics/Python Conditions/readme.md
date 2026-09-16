# Python Conditions and If statements
Python supports the usual logical conditions from mathematics:
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the if keyword.

# How If Statements Work
The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.

# Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
# Note: You can use spaces or tabs for indentation, but you must use the same amount of indentation for all statements within the same code block.

# Multiple Statements in If Block
You can have multiple statements inside an if block. All statements must be indented at the same level.

# Using Variables in Conditions
Boolean variables can be used directly in if statements without comparison operators.

# The Elif Keyword
The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
# Multiple Elif Statements
You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.
# When to Use Elif
Use elif when you have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate if statements because Python stops checking once it finds a true condition.

# Python Else Statement
The Else Keyword
The else keyword catches anything which isn't caught by the preceding conditions.
The else statement is executed when the if condition (and any elif conditions) evaluate to False.

# Else Without Elif
You can also have an else without the elif:
# How Else Works
The else statement provides a default action when none of the previous conditions are true. Think of it as a "catch-all" for any scenario not covered by your if and elif statements.
Note: The else statement must come last. You cannot have an elif after an else.

# Complete If-Elif-Else Chain
You can combine if, elif, and else to create a comprehensive decision-making structure.

# Else as Fallback
The else statement acts as a fallback that executes when none of the preceding conditions are true. This makes it useful for error handling, validation, and providing default values.

# Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.
Note: You still need the colon : after the condition.
# Short Hand If ... Else
If you have one statement for if and one for else, you can put them on the same line using a conditional expression:
note:This is called a conditional expression (sometimes known as a "ternary operator").
# Assign a Value With If ... Else
You can also use a one-line if/else to choose a value and assign it to a variable:
Note :-variable = value_if_true if condition else value_if_false

# Multiple Conditions on One Line
You can chain conditional expressions, but keep it short so it stays readable: