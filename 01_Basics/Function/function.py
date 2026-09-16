print("............Creating a Function...............")

def my_function():
  print("hello")
my_function()

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
