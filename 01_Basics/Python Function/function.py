print("....................Python Function................")


def my_function(name):  # name is a paramiter
    print("Hello", name)

my_function("Aditya")

print("....................Python Function : Number of Arguments................")
''' By default, a function must be called with the correct number of arguments.
If your function expects 2 arguments, you must call it with exactly 2 arguments.'''

def my_function1(fname,lname):
  print(fname + lname )
my_function1("Email", "Refsnes")

print("....................Python Function : Default Parameter Values................")
"You can assign default values to parameters. If the function is called without an argument, it uses the default value:"

def my_function3(name = "friends"):
  print("Hello" , name)
my_function3("Email")
my_function3("Aita")
my_function3()
my_function3("Lasbin")
