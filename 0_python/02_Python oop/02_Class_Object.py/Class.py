print("...........To Create a Cass...........")

class myClass:
  x = 5
  y = 6
  z = 7
k = myClass()

print (myClass)

print("...............To create .....................")

p1 = myClass()
print(f" This is an obect : {p1.x}")

print("...............To Delete Objects .....................")
del p1

print("...............To create  Multiple Objects .....................")
# You can create multiple objects from the same class:

p1 = myClass()
p2 = myClass()
p3 = myClass()

print(p1.x)
print(p2.y)
print(p3.z)
# Note: Each object is independent and has its own copy of the class properties.

print("...............The pass Statement.....................")
class Person:
  pass

