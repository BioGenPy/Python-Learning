print("...................The while Loop.......................")

i = 1 
while i < 6:
  print(i)
  i += 1

print("...................The break Statement.......................")
i = 1
while  i < 6 :
  print(i)
  if i == 4:
    break
  i += 1
print("...................The continue Statement.......................")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("...................The else Statement.......................")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.
i = 1
while i < 6 :
  print(i)
  i += 1 
else:
  print("i is no longer less than 6 ")