print(".............The Length of an Array...........")

cars = ["Ford","Volvo","BMW"]
# Note: The length of an array is always one more than the highest array index.
x = len(cars)
print(x)

print("-------------Looping Array Elements----------")
for x in cars:
    print(x)
print("-------Adding Array Elements--------")
cars.append("honda")
print(cars)

print("-------------Removing Array Elements----------")
cars.pop(1)
print(cars)

print("----------Delete the element that has the value ------")
cars.remove("Volvo")

