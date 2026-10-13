from sys import platform

import module as mx

import platform as pf



print("............This test modules.................")


mx.greeting("hi this test module")

print("............Variables in Module.................")
a = mx.person1["age"],["country"]
print(a)

print("------------Built-in Modules: Built-in Modules : system ......... ")


x = pf.system()
print(x)

print("------------Built-in Modules: Built-in Modules : dir ......... ")
# Note: The dir() function can be used on all modules, also the ones you create yourself.
y = dir(pf)
print(y)

from module import person1
print(".............from import ............")
print(person1["country"] ,["age"])