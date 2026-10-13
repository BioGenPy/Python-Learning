print("....................Basic Decorator................")
# Define the decorator first, then apply it with @decorator_name above the function.

def changecase5(func):
  def myinner():
    return func().upper()
  return myinner

@changecase5
def myfunction55():
  return "Hellow Aditya"

print(myfunction55())

print("----------------- Multiple Decorator Calls ------------------------")
# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.


def myDecorate(func):
  def myinner():
    return func().upper()
  return myinner
@myDecorate
def myfunction3():
  return " Hello Aditya"

@myDecorate
def otherfunction():
  return " i am speed !"

print(myfunction3())
print(otherfunction())

print("---------------------- Arguments in the Decorated Function---------------------")
# Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function:

def changecase1(func):
  def myinner1(x):
    return func(x).upper()
  return myinner1
@changecase1
def myFun(nam):
  return "Hello" + nam
print(myFun("aditya"))

print("-------------------*args and **kwargs-------------------")

def change(func):
  def myinner(*args, **kwargs):
    return func(*args ,**kwargs).upper()
  return myinner
@change
def myFunction(man):
  return "Hello" + man

print(myFunction("aditya"))

print("-----------------Decorator With Arguments ---------------------------")
# Decorators can accept their own arguments by adding another wrapper level.

def chanCase(n):
  def chanCase(fun):
    def myinner():
      if n == 1:
        a = fun().lower()
      else:
        a = fun().upper()
        return a
      return myinner
    return chanCase
  @chanCase(1)
  def myfunction33():
    return ": Hello Aditya"
  print(myfunction3())


print("-----------------Multiple Decorator Calls-------------------------")
# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction5():
  return "Tobias"

print(myfunction5())

print("---------------------Preserving Function Metadata----------------------")
def metafunction():
  return "Have a greate day !"
print(metafunction.__name__)


import functools

def changeFunction(funcn):
  @functools.wraps(funcn)
  def myinner():
    return funcn().upper()
  return myinner

@changeFunction
def myfunction():
  return "Have a greate day !"
print(myfunction.__name__)
  