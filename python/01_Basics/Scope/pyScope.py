print("..................Local Scope...............")


def myFunc():
  x = 30
  print(x)
myFunc()

print(".........Function Inside Function........")


def insideFunction():
  y = 300
  def myinnerFunction():
    print(y)
  myinnerFunction()
insideFunction()

p = 500

def myGlobalFunction():
  print(p)
myGlobalFunction()
print()

print(".........Naming Variables........")

u = 300
def myNamingFunction():
  u = 400
  print("Innerfunction :",u)
myNamingFunction()
print("Outer function :" ,u)

print(".........Global Keyword........")

def globalFunction():
  global g
  g = 600
globalFunction()
print("Global keyword :",g)

print(".........Nonlocal Keyword.......")


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

print(".........The LEGB Rule.......")

x = "Global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner :", x)
  inner()
  print("Outer :", x)
outer()
print("Global : ", x )