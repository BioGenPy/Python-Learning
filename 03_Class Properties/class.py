print("...................Class Properties.................")

class Property:

    def __init__(self, house, area):
        self.house = house
        self.area = area

c = Property("palace", 250)

print(c.house)
print(c.area)

print("-----------Access Properties------------")

class student:
  def __init__(self,name,Class,roll,age):
    self.name = name
    self.Class = Class 
    self.roll = roll
    self.age = age 

s = student("Aditya","one",5,15)

print (f"Student name :{s.name} \n Student Roll is : {s.roll} \n Student age is :{s.age} \n Student Class is :{s.Class} \n Student age is : {s.age}")

print("-----------Modify Properties------------")

s2 = student("Susmita","nine",25,30)
print(
    f"Student name :{s2.name} \n Student Roll is : {s2.roll} \n Student age is :{s2.age} \n Student Class is :{s2.Class} \n Student age is : {s2.age}"
)

print("-----------Delete Properties------------")


s3 = student("Susmita", "nine", 25, 30)
# del s3.age
print(
    f"Student name :{s3.name} \n Student Roll is : {s3.roll} \n Student age is :{s3.age} \n Student Class is :{s3.Class} \n Student age is : {s2.age}" # s3 has been deleted
)
print("-----------Class Properties vs Object Properties------------")
class software:
  application = "web base" # Class property
  
  
  def __init__(self,softwareName):
    self.softwareName = softwareName # Instance property

s1 = software("Tally")
s2 = software("antivairous")

print(s1.softwareName) 
print(s2.softwareName) 
print(s1.application) 
print(s2.application) 

print("-----------Modifying Class Properties------------")
# When you modify a class property, it affects all objects:
# Change a class property:

class Person25:
  lastname = ""
  
  def __init__(self, name):
    self.name = name

t = Person25("Aditya")
t2 = Person25("Samir")

Person25.lastname = "Rahit"
print(t.lastname)
print(t2.lastname)


print("-----------Add New Properties------------")
# Note: Adding properties this way only adds them to that specific object, not to all objects of the class.
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


# Now you pass all the information when creating the object
p1 = Person("Ratan", 25, "Gaighata")

print(p1.name)
# Output: Ratan

print(p1.age)
# Output: 25

print(p1.city)
# Output: Gaighata
