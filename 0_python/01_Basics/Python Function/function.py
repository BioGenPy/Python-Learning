from turtle import pen, pos


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

print("....................Python Function : Keyword Arguments................")
# You can send arguments with the key = value syntax.

def keyAguments ( book, author):
  print("I have a book name is " , book)
  print("Author is ", author)
keyAguments(book = "Discovery of india " ,  author = "Pandit jhwralneharu")

print("....................Python Function : Positional Arguments...............")

''' When you call a function with arguments without using keywords, they are called positional arguments.
Positional arguments must be in the correct order: '''

def positionalArguments(book,author):
  print("I have a book name is " ,book)
  print("The book Author name is " , author)
positionalArguments("Discovery of india ", "Jwharalneharu")

print("....................Python Function : Mixing Positional and Keyword Arguments...............")

def mixingPositionalAndKeywordArguments(studen,name,age):
  print("I am a " ,studen ,"My  Name is ", name , " I am  ", age, "Years old")
mixingPositionalAndKeywordArguments("Student",name = "Aditya",age=5)

print("....................Python Function : Passing Different Data Types...............")
# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
# ----Sending a list as an argument:
print("----Sending a list as an argument:")
def my_fruitsFunction(fruits):
  for fruit in fruits:
    print(fruit)
my_fruits_list =["apple","Banana","orange","charry","oava","lemon"]
my_fruitsFunction(my_fruits_list)

print("----Sending a dictionary as an argument::")
def personfunction(person):
  print("name :",person["name"])
  print("Age :" ,person["age"])
my_person = {"name" : "Aditya", "Age is ": 5}
print(my_person)

print("----Return Values:")

# Functions can return values using the return statement:

def my_returnFunction(x , y):
  return x + y

result = my_returnFunction( 5,6)
print(result)

print("....................Python Function : Returning Different Data Types...............")

print("............Returning A function that returns a list: : >")
# Functions can return any data type, including lists, tuples, dictionaries, and more.
def returnDifferenceDataTypes():
  return["apple" ,"Banana", "Lemon"]

fruits = returnDifferenceDataTypes()
print(fruits[0])
print(fruits[1])
print(fruits[2])

