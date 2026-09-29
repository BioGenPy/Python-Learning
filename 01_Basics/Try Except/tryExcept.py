from signal import raise_signal
from sys import exception


print(".............Exception Handling................")
# The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("An exception occureed")

print(".............Many Exceptions...........")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print(".............Else Handling................")

try:
    print("hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

print(".............Finally Handling................")
# This can be useful to close objects and clean up resources:
try:
    print("f")
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
print(".............Example................")

# Try to open and write to a file that is not writable:

try:
    f = open("demofile.txt")
    try:
        f.write("lorum ipsum")
    except:
        print("Something went wrong when write to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

print("............Raise an exception.............")
# As a Python developer you can choose to throw an exception if a condition occurs.

rx = -1
if rx < 0:
    raise Exception("Sorry, no numbers below zero")
print("............The raise keyword is used to raise an exception.............")
# You can define what kind of error to raise, and the text to print to the user.

x = "hello"
if not type(x) is int:
  raise TypeError("only integers are allowed")
