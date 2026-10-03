


print("--------------------Python Magic Methods---------------------------")
# __init__() and __str__() are both magic methods:


class Person:
  def __init__(self,name):
    self.name = name 
  
  def __str__(self):
    return f"Person : {self.name}"

p1 = Person("Aditya")
print(p1)

print("--------------------The __init__() Method---------------------------")
# All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
class animal:
  def __init__(self,name,age):
    self.name = name 
    self.age = age 
a = animal("dog",34)
print(a.name)
print(a.age)

print("--------------------Default Values in __init__()---------------------------")
# You can also set default values for parameters in the __init__() method:

class car:
  def __init__(self,model, year =2024, color="red",brand = "Mercides"):
    
    self.model = model 
    self.year = year
    self.color = color
    self.brand = brand
d = car("Tata sumo",2026,"yellow","heoro")


print(d.model,d.year,d.color,d.brand)

# The __str__() method is a magic method that controls what is returned when the object is printed, or passed to str().
# __str__() must return a string. If it returns anything else, Python raises a TypeError.

class student:
  def __init__(self,name,stander,school):
    self.name = name
    self.stander = stander
    self.school = school
  
  def __str__(self):
    return f"Student Name :{self.name} \n Study in Class: {self.stander} \n School Name: {self.school}"
s = student("Aditya",44,"Aditya acedemy")
print(s)

class stringExample:
  def __init__(self,age):
    self.age = age 
  
  def __str__(self):
    return self.age

strx = stringExample(25)
# print(strx)

class Employee:
  def __init__(self,name,age):
    self.name = name 
    self.age = age 
  
  def __repr__(self):
    return f"Employee name: {self.name} \n age: {self.age} "
e = Employee("Animesh",34)
print(e)


class Teacher:
  def __init__(self,name,age):
    self.name = name
    self.age = age 
  
  def __str__(self):
    return f"{self.name} {self.age}"
  
  def __reper__(self):
    return f"Teacher(name={self.name} age = {self.name}"

t = Teacher("Aditya",6)
print(t)
# Note: __str__() gives a short, readable text. __repr__() gives a more technical result, that looks like the code needed to recreate the object.


class Doctor:
  def __init__(self,name,age):
    self.name = name
    self.age = age 
  
  def __eq__(self,other):
    return self.name == other.name and self.age == other.age


d = Doctor("aditya",30)

d1 = Doctor("Aditya",30)

print(d == d1)
# Note: Did you notice the parameter other? It represents the other object being compared to.
"""Change how to Compare
Add __eq__() to define what "equal" means for your class:"""


class Driver:
  def __init__(self,name,age):
    self.name = name
    self.age = age 
  def __add__(self,other):
    return self.age + other.age 

d = Driver("Aritro",22)
d1 = Driver("Aritro",22)

print(d1 + d )
# Note: Without __add__(), writing p1 + p2 would raise a TypeError, since Python would not know how to add two Person objects.

# The __len__() method controls what the built-in len() function returns for your object.

class Company:
  def __init__(self,employees):
    self.employees = employees
  
  def __len__(self):
    return len(self.employees)
c1 = Company(["Aditya","Tapan","Sujit"])
print(len(c1))
# Note: Without __len__(), calling len(c1) would raise a TypeError, since Python would not know what "length" means for a Company.

class Developer:
  def __init__(self,name,age):
    self.name = name 
    self.age = age
  
  def __lt__(self,other):
    return self.age < other.age 
d1 = Developer("Adity",30)
d2 = Developer("Dhiraj",25)

print(d1 < d2)
"""Compare Without __lt__()
Without __lt__(), comparing two objects with < raises an error:"""

print("--------------------Sorting with __lt__()---------------------------")
# Python also uses __lt__() to sort objects, with functions like sorted().
class Worker:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def __lt__(self,other):
        return self.age < other.age
p1 = Worker("Emil", 22)
p2 = Worker("Tobias", 19)
p3 = Worker("Linus", 15)

x = sorted([p1,p2,p3])

print(x[0].name)
"""Note: sorted() returns a new list, ordered by age.

x[0] is the Person with the lowest age.

You can sort as many objects as you like - not just two or three."""

class Student:
  def __init__(self,name):
    self.name = name
  
  def __contains__(self,name):
    return name in self.name

s = Student(["aditya","Rajib","animesh"])

print("aditya" in s)


print("--------------------The __call__() Method---------------------------")
# The __call__() method lets an object be called like a function, using object() syntax.



class clickCounter:
    def __init__(self):
        self.clicks = 0

    def __call__(self):
        self.clicks += 1
        return self.clicks 

button_cliks = clickCounter()

print(button_cliks())
print(button_cliks())
print(button_cliks())
print(button_cliks())
