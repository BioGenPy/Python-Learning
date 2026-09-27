x = "awesome"
def myFunction():
    x = "fantastic"

    print("Ptyhon is " + x)
myFunction()
print("Python is " + x)

def myGlobal():
    global x
    x = "fantastic"
myGlobal()
print("Python is " + x)
