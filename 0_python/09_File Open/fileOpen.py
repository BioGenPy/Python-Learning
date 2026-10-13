import os
print("------------open() Function-----------------")
f = open("demofile.txt","r")
print(f.read())
f.close()

f = open("C:\\Users\Kamalesh\Desktop\myfiles\welcome.txt")
print(f.read())
f.close()
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")