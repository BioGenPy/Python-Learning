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
