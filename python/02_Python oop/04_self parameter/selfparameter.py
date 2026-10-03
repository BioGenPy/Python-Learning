from typing import Self


print("............The self Parameter..............")
# Use self to access class properties:
# Note: The self parameter must be the first parameter of any method in the class.
# The self parameter links the method to the specific object:
class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age 
  
  def greet(self):
    print("Hello, my name is " + self.name)
p1 = Person("Aditya",25)
p1.greet()


class Student:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)


p1 = Student("Tobias")
p2 = Student("Linus")

p1.printname()
p2.printname()

print("............self Does Not Have to Be Named self " )
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:
# Use the words myobject and abc instead of self:
# Note: While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.
class Person:
  def __init__(Self,name, age):
    Self.name = name
    Self.age = age 
  def greet(abc):
    print("Hello my name is " + abc.name,)
p3 = Person("Aditya",36)
p3.greet()


print("......Accessing Properties with self.....")

class Car:
  def __init__(self,brand,model,year):
    self.brand = brand 
    self.modle = model 
    self.year = year
  
  def display_info(self):
    print("f{self.year}{self.model}{self.year}")

car1 = Car("Toyota","Corolla",2026)
car1.display_info()


print("..........Calling Methods with self............")
# Call one method from another method using self:
class family:
  def __init__(self,person):
    self.name = person
  
  def greet(self):
    return "hello,  " + self.name
  
  def welcome(self):
    message = self.greet()
    print(message + "! welcome to our family")
    
    
f1 = family("Mridha")
f1.welcome()
