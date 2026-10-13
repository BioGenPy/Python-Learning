## Python Encapsulation

Encapsulation is about protecting data inside a class.

It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

This prevents accidental changes to your data and hides the internal details of how your class works.

## Private Properties

In Python, you can make properties private by using a double underscore `__` prefix:

## Why Use Encapsulation?

Encapsulation provides several benefits:

* **Data Protection:** Prevents accidental modification of data
* **Validation:** You can validate data before setting it
* **Flexibility:** Internal implementation can change without affecting external code
* **Control:** You have full control over how data is accessed and modified

**Note:** A single underscore `_` is just a convention. It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction.

## Name Mangling

Name mangling is how Python implements private properties and methods.

When you use double underscores `__`, Python automatically renames it internally by adding `_ClassName` in front.

For example, `__age` becomes `_Person__age`.
