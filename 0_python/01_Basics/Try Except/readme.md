# Python **Try Except**

The `try` block lets you test a block of code for errors.

The `except` block lets you handle the error.

The `else` block lets you execute code when there is no error.

The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling

When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the `try` statement:

## Built-in Exceptions

The table below shows built-in exceptions that are usually raised in Python:


| Exception                                                                                 | Description                                                                       |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [ArithmeticError](https://www.w3schools.com/python/ref_exception_arithmeticerror.asp)     | Raised when an error occurs in numeric calculations                               |
| [AssertionError](https://www.w3schools.com/python/ref_exception_assertionerror.asp)       | Raised when an assert statement fails                                             |
| [AttributeError](https://www.w3schools.com/python/ref_exception_attributeerror.asp)       | Raised when attribute reference or assignment fails                               |
| Exception                                                                                 | Base class for all exceptions                                                     |
| EOFError                                                                                  | Raised when the input() method hits an "end of file" condition (EOF)              |
| FloatingPointError                                                                        | Raised when a floating point calculation fails                                    |
| GeneratorExit                                                                             | Raised when a generator is closed (with the close() method)                       |
| [ImportError](https://www.w3schools.com/python/ref_exception_importerror.asp)             | Raised when an imported module does not exist                                     |
| [IndentationError](https://www.w3schools.com/python/ref_exception_indentationerror.asp)   | Raised when indentation is not correct                                            |
| [IndexError](https://www.w3schools.com/python/ref_exception_indexerror.asp)               | Raised when an index of a sequence does not exist                                 |
| [KeyError](https://www.w3schools.com/python/ref_exception_keyerror.asp)                   | Raised when a key does not exist in a dictionary                                  |
| KeyboardInterrupt                                                                         | Raised when the user presses Ctrl+c, Ctrl+z or Delete                             |
| LookupError                                                                               | Raised when errors raised cant be found                                           |
| MemoryError                                                                               | Raised when a program runs out of memory                                          |
| [NameError](https://www.w3schools.com/python/ref_exception_nameerror.asp)                 | Raised when a variable does not exist                                             |
| NotImplementedError                                                                       | Raised when an abstract method requires an inherited class to override the method |
| OSError                                                                                   | Raised when a system related operation causes an error                            |
| [OverflowError](https://www.w3schools.com/python/ref_exception_overflowerror.asp)         | Raised when the result of a numeric calculation is too large                      |
| ReferenceError                                                                            | Raised when a weak reference object does not exist                                |
| RuntimeError                                                                              | Raised when an error occurs that do not belong to any specific exceptions         |
| StopIteration                                                                             | Raised when the next() method of an iterator has no further values                |
| SyntaxError                                                                               | Raised when a syntax error occurs                                                 |
| TabError                                                                                  | Raised when indentation consists of tabs or spaces                                |
| SystemError                                                                               | Raised when a system error occurs                                                 |
| SystemExit                                                                                | Raised when the sys.exit() function is called                                     |
| [TypeError](https://www.w3schools.com/python/ref_exception_typeerror.asp)                 | Raised when two different types are combined                                      |
| UnboundLocalError                                                                         | Raised when a local variable is referenced before assignment                      |
| UnicodeError                                                                              | Raised when a unicode problem occurs                                              |
| UnicodeEncodeError                                                                        | Raised when a unicode encoding problem occurs                                     |
| UnicodeDecodeError                                                                        | Raised when a unicode decoding problem occurs                                     |
| UnicodeTranslateError                                                                     | Raised when a unicode translation problem occurs                                  |
| [ValueError](https://www.w3schools.com/python/ref_exception_valueerror.asp)               | Raised when there is a wrong value in a specified data type                       |
| [ZeroDivisionError](https://www.w3schools.com/python/ref_exception_zerodivisionerror.asp) | Raised when the second operator in a division is zero                             |

## Definition and Usage

The `raise` keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.
