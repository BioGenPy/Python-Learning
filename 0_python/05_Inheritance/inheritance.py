print("----------------Create a parent Class--------------")
# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self,fname,lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Aditay","Dipika")
x.printname()
print("----------------Create a Child Class--------------")
# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):

    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.goodname = fname
        self.surname = lname
        self.graduationyer = year

    def welcome(self):
        print(
            "welcome",
            self.goodname,
            self.surname,
            "To the class of ",
            self.graduationyer
        )


x = Student("Aditay", "Mridha",2026)
x.welcome()
