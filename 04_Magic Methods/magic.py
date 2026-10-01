print("--------------------Python Magic Methods---------------------------")
# __init__() and __str__() are both magic methods:


class Person:
  def __init__(self,name):
    self.name = name 
  
  def __str__(self):
    return f"Person : {self.name}"

p1 = Person("Aditya")
print(p1)