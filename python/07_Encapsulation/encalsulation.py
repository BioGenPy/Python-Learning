print("........Private Properties............")

class Person1:

    def __init__(self, name, age):
        self.name = name
        self._age = age  # Private property # Protected property
# You can also make methods private using the double underscore prefix:

p1 = Person1("Adity",25)

print(p1.name)
# print(p1.__age)
# Note: Private properties cannot be accessed directly from outside the class.

print("........Get Private Property Value............")
class Person2:
  def __init__(self,name,age):
    self.name = name 
    self.__age = age 
  
  def get_age(self):
    return self.__age 

p1 = Person2("Tobias",25)
print(p1.get_age())

print("........Set Private Property Value............")

class Student:
  def __init__(self,name,age):
    self.name = name
    self.__age = age 
  
  def get_age(self):
    return self.__age 
  
  def set_age(self,age):
    if age > 0 :
      self.__age = age 
    else:
      print("Age must be possative") 
p1 = Student("Sujit",26)
print(p1.get_age()) 

print("-----------Name Mangling---------------")
# See how Python mangles the name:
class Developer:
    def __inti__(self,name,age):
        self.name = name 
        self.__age = age 
p1 = Developer("Aditya", 30)

print(p1)
