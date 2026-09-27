print("............Creating a Function...............")

def my_functionTest():
  print("hello")
my_functionTest()

def fahrenhheit_to_celsius(fahrenheit):
  return(fahrenheit - 32) * 5/9
print(fahrenhheit_to_celsius(77))
print(fahrenhheit_to_celsius(95))
print(fahrenhheit_to_celsius(50))

print("............Return Values...............")
def get_greeting():
  return  "Hello from a function"
message = get_greeting()
print(message)

def get_greeting1():
  return "Hello From a function1"
print(get_greeting1())

print("............The pass Statement...............")
def my_function1():
  pass
print("............Function Arguments...............")

def my_function(fname): # name is parameter
  print("hello" ,fname)
my_function("Email") # Email is an argument

print("............Function Arguments2...............")

def myFunction(fname ,lname):
  print(fname + " " + lname)
myFunction("fname","lname")

print("............Default Parameter Values...............")
def my_function5(country = "Norway"):
  print("I am from", country)

my_function5("Sweden")
my_function5("India")
my_function5()
my_function5("Brazil")

print("............Keyword Arguments...............")
# This way, with keyword arguments, the order of the arguments does not matter.
# The phrase Keyword Arguments is often shortened to kwargs in Python documentation.
def kewordArguments(animal,name):
  print("I have a ", animal )
  print("My" , animal + " s name is ", name)
kewordArguments(animal= "dog", name="Buddy")

print("............Positional Arguments...............")
'''When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:'''
def positinaArguments(animal,name):
  print("i have a ",animal)
  print("my",animal + "  s name " ,name)
positinaArguments("dog","buddy")

# The order matters with positional arguments:

def positinaArguments1(animal,name):
  print("i have a ",animal)
  print("my",animal + "  s name " ,name)
positinaArguments1("buddy","dog")

print("...........Mixing Positional and Keyword Arguments.............")

def mixing_positional_keyword_arguments(animal,name,age):
  print(" I have a ", age ,"Yera old", animal, "name", name  )
mixing_positional_keyword_arguments("dog", name = "Buddy",age = 5)

print("...........Passing Different Data Types.............")

'''You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
The data type will be preserved inside the function:'''

# Sending a list as an argument:

def passingstrDataType(fruit):
   print("Passing String Data Type:")
   for fruit in fruit:
       print(fruit)
   
my_fruits = ["apple","Banana","cherry"]
passingstrDataType(my_fruits) 

# Sending a dictionary as an argument:

def my_dectionaryArguments(person):
  
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name" : "Aditya", "age" : 25}
my_dectionaryArguments(my_person)

# Functions can return values using the return statement:
def returnFunction(x, y):
  return x + y 
result = returnFunction (5,4)
print(result)

print("------------------Returning Different Data Types---------------")
# Functions can return any data type, including lists, tuples, dictionaries, and mo
  # A function that returns a list:
print("------------------A function that returns a list:---------------")

def listFunction():
  return["apple",'banana','cherry']
fruit = listFunction()
print(fruit [0])
print(fruit [1])
print(fruit [2])

print("-------------A function that returns a tuple:-------------")
def tupleFunction():
  return( 10,20)
x,y = tupleFunction()

print("X : " , x)
print("y : ", y)


print("-------------Positional-Only Arguments-------------")

'''You can specify that a function can have ONLY positional arguments.

To specify positional-only arguments, add , / after the arguments:'''

def positionalFunction(name, /):
  print("Hello" ,name )
positionalFunction("Aditya")

print("-------------Keyword-Only Arguments-------------")

def keywordOnlyFunction(*, name):
  print("Hello", name)
keywordOnlyFunction(name = "Ratan")

print("-------------Combining Positional-Only and Keyword-Only-------------")

# Arguments before / are positional-only, and arguments after * are keyword-only:

def combineArguments(a,b,/,*,c,d):
  return a + b + c + d
res = combineArguments(5, 10,  c=5, d=5)
print(res)

print("-------------Python *args and **kwargs-------------")

'''*args and **kwargs
By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept a unknown number of arguments.'''
print("-------------Arbitrary Arguments - *args-------------")

'''If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly:'''

# Using *args to accept any number of arguments:

def arbitaryFunction(*kids):
  print("The youngest child is : " + kids[3])
arbitaryFunction("animesh","rohan","sudip","ranu")

print("......................................... Accessing individual arguments from *args:..............")

def accessingFunction(*args):
  print("Type : ", type(args))
  print("First argument : ", args[0])
  print("Second argument : ", args[1])
  print("All arguments : ", args[2])
accessingFunction("animesh","Dipika","Aditya","Susmita")

print("----------------Using *args with Regular Arguments-------------")
''' Regular parameters must come before *args:   '''

def argusWithRegular(greeting, *names):
  for name in names:
    print(greeting,name)
argusWithRegular("Hello","Aprna","Susmita","Ranu")

# *args is useful when you want to create flexible functions:

def my_calculation(*numbers):
  total = 0 
  for num in numbers:
    total += num
  return total
print(my_calculation(1,2,3,4))
print(my_calculation(40,50,70,44445))
print(my_calculation(5))

def kwargsFunction(**kid):
  print("His last name is " + kid['lname'])
kwargsFunction(fname = "Aditya ",  lname = "Mridha")

print("................Accessing values from **kwargs:..................")


def kwargsFun(**myvar):
  print("Type : ", type(myvar))
  print("Name : ", type(myvar))
  print("Age : ", type(myvar))
  print("All data : ", type(myvar))
kwargsFun(name = "ram", age = 30, city = "kolkata")

print("................Using **kwargs with Regular Arguments:..................")
# Regular parameters must come before **kwargs:

def kwatFunction(username,**details):
  print('Username', username)
  print("Aditional details :")
  for key, value in details.items():
    print("" ,key + ":", value)
kwatFunction("email1234", age = 25, city = "kolkata" ,hoby = 'coding')


print("................Combining *args and **kwargs..................")

def argsAndKwargs(title,*args,**kwargs):
  print("Title : ", title)
  print("Positional arguments : ", args)
  print("keyword arguments : ", kwargs)
argsAndKwargs("User Info", 'Aditya', "Samir" ,age = 30 , city = "kolkata")

print("................Unpacking Arguments..................")

''' The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments. '''

def unpackingFunction(a,b,c):
  return a + b + c 
nums = [1,2,3]
rest = unpackingFunction(*nums)
print(rest)

print(".............................Unpacking Dictionaries with **...................")
# If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

def unpackDict(fname,lname):
  print("Hello",fname,lname)
person = {"fname" : "Aditya","lname": "Refsnes"}
unpackDict(**person) # Use * and ** in function definitions to collect arguments, and use them in function calls to unpack arguments.
