## What are Magic Methods?

Magic methods are special methods whose names start and end with double underscores, like `__init__()` and `__str__()`. Because of the double underscores, they are also called **dunder methods** (short for "double underscore").

You do not call magic methods directly. Python calls them for you, automatically, in certain situations - like when an object is created, printed, or compared to another object.

**Note:**`__init__()` runs automatically when an object is created, and `__str__()` runs automatically when the object is printed.

## List of Magic Methods

This tutorial covers the following magic methods. Click a method to see a full lesson with examples:


| Method           | Called By               | Description                                              |
| ------------------ | ------------------------- | ---------------------------------------------------------- |
| `__init__()`     | `Person(...)`           | Runs when a new object is created                        |
| `__str__()`      | `print(obj)`,`str(obj)` | Controls the readable text shown for an object           |
| `__repr__()`     | `repr(obj)`             | Controls the developer-facing representation             |
| `__eq__()`       | `obj1 == obj2`          | Controls what "equal" means for the class                |
| `__add__()`      | `obj1 + obj2`           | Controls what the`+`operator does                        |
| `__len__()`      | `len(obj)`              | Returns the "length" of an object                        |
| `__lt__()`       | `obj1 < obj2`           | Controls how objects are ordered when compared or sorted |
| `__contains__()` | `item in obj`           | Controls what the`in`operator checks                     |
| `__call__()`     | `obj(...)`              | Lets an object be called like a function                 |

## The __init__() Method

All classes have a built-in method called `__init__()`, which is always executed when the class is being initiated.

The `__init__()` method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

**Note:** The `__init__()` method is called automatically every time the class is being used to create a new object.

## Why Use __init__()?

Without the `__init__()` method, you would need to set properties manually for each object:

Using `__init__()` makes it easier to create objects with initial values:

## Default Values in __init__()

You can also set default values for parameters in the `__init__()` method:

## Multiple Parameters

The `__init__()` method can have as many parameters as you need:

## The __str__() Method

The `__str__()` method is a magic method that controls what is returned when the object is printed, or passed to `str()`.

`__str__()` must return a `string`. If it returns anything else, Python raises a `TypeError`.

## The __repr__() Method

While `__str__()` controls the readable, user-facing text shown when you print an object, `__repr__()` controls a more technical representation, meant for developers.

**Note:** This class has no `__str__()` method, so Python falls back to `__repr__()` when the object is printed.

## __str__() vs __repr__()

When a class defines both `__str__()` and `__repr__()`, `print()` uses `__str__()`, while the built-in `repr()` function always uses `__repr__()`:

## The __eq__() Method

Most data types (string, number, list, etc) compare *by content* when you use `==` to compare them.

For objects, this is not the case. The `==` operator checks if the two variables point to the exact same object in memory - not if their content matches.

The `__eq__()` method allows you to change this behavior.

## The __add__() Method

Magic methods can control what happens when you use an operator, like `+`, on your own objects. This is called  **operator overloading** .

## The __len__() Method

The `__len__()` method controls what the built-in `len()` function returns for your object.

## The __lt__() Method

The `__lt__()` method ("less than") controls what the `<` operator does for your own objects.

## The __contains__() Method

The `__contains__()` method controls what the `in` operator checks for your own objects.

## The __call__() Method

The `__call__()` method lets an object be called like a function, using `object()` syntax.
