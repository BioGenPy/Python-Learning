print("..............Python For Loops..................")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  print(type(fruits))
  
print("..............Looping Through a String..................")
for f in "apple":
  print(f)

print("..............The break Statement.................")
# Exit the loop when x is "banana":

car = ["Sumo","suzuku","mohindra"]
for c in car :
  print(c)
  if c == "suzuku":
    break
print("..............break comes before the print.................")  
car = ["Sumo","suzuku","mohindra"]
for c in car :
  if c == "suzuku":
    break
  print(c)
  
print("..............The continue Statement.................")
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
color = ["red","Green","Yellow","Blue"]
for h in color:
  if h == "Yellow":
    continue
  print(h)

print("..............The range() Function.................")
''' The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. '''
#number = [1,2,3,4,5,6,7]
# range(2, 6), which means values from 2 to 6 (but not including 6):
for n in range(6): #Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
  print(n)
print("..............")
for m in range(3,10):
  print(m)

print("..............Else in For Loop.................")
for v in range(6):
  if x == 3: break
  print(v)
else:
  print("Finally finishded ! ")
  
print("..............Nested Loops.................")
  # The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red","big","testy"] 
fruits = ["apple", "banana", "cherry"]
for d in adj:
  for f in fruits:
    print(d,f) 
print("..............The pass Statement.................")
''' for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error. '''

for k in [0,1,2,3]:
  pass

