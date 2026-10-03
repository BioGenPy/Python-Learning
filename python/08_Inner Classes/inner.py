print("---------Create an inner class:--------------")
class Outer:
  def __init__(self):
    self.name = "Outer class"
  
  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name)

print("--------------Accessing Inner Class from the Outside----------------")

outer1 = Outer()
inner = outer1.Inner()
inner.display()

print("--------------display----------------")

class Outer1:
  def __init__(self):
    self.name = "Aditya"
  
  class Inner1:
    def __init__(self,outer):
      self.outer = outer
    
    def display(self):
      print(f"outer class name : {self.outer.name}")

outer = Outer1()
inner = outer.Inner1(outer)
inner.display()


print(
    "......Inner classes are useful for creating helper classes that are only used within the context of the outer class:...."
    
)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = "Off"

        def start(self):
            self.status = "Running"
            print("Engine started")

        def stop(self):
            self.status = "Off"
            print("Engine stopped")

    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first!")


car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()


print("----------Multiple Inner Classes------------")
class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()
    
  class CPU:
    def process(self):
      print("Pocessing data.....................")
      
  class RAM:
    def store(self):
      print("Storing data ..................")
computer = Computer()
computer.cpu.process()
computer.ram.store()     
