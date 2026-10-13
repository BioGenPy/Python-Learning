print("-------------------Function Polymorphism-----------------")
print("------String--------")
# For strings len() returns the number of characters:
x = "Hello World"
print(len(x))

print("------Tuple--------")
mytuple = ('apple',"banana","cherry")
# For tuples len() returns the number of items in the tuple:
print(len(mytuple))

# For dictionaries len() returns the number of key/value pairs in the dictionary:

thisdisct ={
  "brand" : "ford","model":"Mustang","year":1964
  
}
print(len(thisdisct))

print("------Class Polymorphism--------")
class Car:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model 
  def move(self):
    print("prinve")

class Boat:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model 
  def move(self):
    print("Sail")

class Plane:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model 
  def move(self):
    print('fly')
car = Car("ford","mustang")
boat = Boat("Ibiza",'Touring 20')
plane =Plane("Boeing","774")

for x in (car,boat,plane):
    x.move()

print("----Inheritance Class Polymorphism------")

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
