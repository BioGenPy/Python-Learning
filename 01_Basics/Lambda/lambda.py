print("....................Lambda Functions.................................")

x = lambda a,b : a*b
print(x(5,6))


y = lambda a,b,c : a+b+c
print(y(5,6,2))

def myfunction(n):
  return lambda a:a*n
mydoubler = myfunction(2)
print(mydoubler(11))


print("-------------------Lambda with Built-in Functions---------------------")
print("--------Using Lambda with map()--------------")
# The map() function applies a function to every item in an iterable:

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
doubled = list(map(lambda x : x *2,numbers))
print(doubled)

print("----Using Lambda with filter()--------------")
# The filter() function creates a list of items for which a function returns True:

numbers = [1,2,3,4,5,6,7,8]
odd_numbers = list(filter(lambda x : x % 2 != 0 , numbers))
print(odd_numbers)

print("----Using Lambda with sorted()--------------")
# The sorted() function can use a lambda as a key for custom sorting:

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

print("----Sort strings by length:()--------------")
words = [ "apple","pie","banana","cherry"]
sorted_word = sorted(words,key=lambda x : len(x))
print(sorted_word)


