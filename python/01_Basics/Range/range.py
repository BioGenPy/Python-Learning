print("......Call range() With One Argument....")

# Create a range of numbers from 0 to 9:
x = range(9)
for i in range(10):
  
  print(i)

print("......Call range() With Two Arguments....")

y = range(3,10)
print(y)

print("......Call range() With Three Arguments....")
z = range(3,10,2)
print(z)

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

print("...............Slicing Ranges...........")

r = range(10)
print(r[2])
print(r[:3])

print("............... membrship.................")
# The return value is True when the number is present in the range, and False when it is not.
r = range(0,10,2)
print(6 in r)
print(7  in r )
print("............... Length .................")
# Ranges support the len() function to get the number of elements in the range.

r = range(0,10,2)
print(len(r))