print("-------Python Iterators----------")
mytupe = ("apple","Banana","Cherry")

myit = iter(mytupe)

print(next(myit))
print(next(myit))
print(next(myit))

print("------------Even strings are iterable objects, and can return an iterator:----------")

mystr = "Banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("-----------Looping Through an Iterator------------")

mytuple = ("Apple","Banana","Cherry")
for x in mytuple:
    print(x)


print("------------Iterate the characters of a string:----------")

mystr = "Bnanan"

for x in mystr :
    print(x)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


print("--------------StopIteration---------------- ")


class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return  x
myclass = MyNumber()
miter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("....................Stop after 20 iterations:........")
class MyNumbers1:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumbers1()
myiter = iter(myclass)

for x in myiter:
    print(x)
