print("..............__init__() Method ...............")
class person(object):
  """docstring for Person."""
  def __init__(self,name, age):
    self.name = name
    self.age = age 
p1 = person("Aditya",36)
print(p1.name)
print(p1.age)

print("..............Create a class without __init__():...............")
# Create a class without __init__():
"""class Person:
    pass


p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age) """


class Person_two:

    def __init__(self, name, age):
        self.name = name
        self.age = age
t1 = Person_two("Liton", 28)
print(t1.name)
print(t1.age)

print("..............Default Values in __init__():...............")
# You can also set default values for parameters in the __init__() method:
# Set a default value for the age parameter:

class Person1:
  
  def __init__(self, name, age=28):
    self.name = name 
    self.age = age 
p1 = Person1("Ratan")
p2 = Person1("Susmita",29)
print(p1.name,p1.age)
print(p2.name,p2.age)

print("..............Multiple Parameters():...............")
# The __init__() method can have as many parameters as you need:
# Create a Person class with multiple parameters:
class Stuednt:
  def __init__(self,name,age,city,country):
    
    self.name = name
    self.age = age 
    self.city = city 
    self.country = country
s1 = Stuednt("Aditya",5,"kolkata","india")
print(s1.name,s1.age,s1.city,s1.country)