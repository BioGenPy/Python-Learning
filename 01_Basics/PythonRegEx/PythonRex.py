print(".............RegEx in Python..............")
import re
# Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in kolkata"
x = re.search("^The.*kolkata$",txt)
print(x)

print(".................The findall() Function...................")


txt1 = "The rain in Spain"
xt = re.findall("ai", txt1)
print(xt)

print(".................Return an empty list if no match was found:...................")
txt2 = "The rain in Spain"
xr = re.findall("Portugal", txt2)
print(xr)

print("..........The search() Function............")
print("..........Search for the first white-space character in the string:............")

import re  # 1. Add this import statement

txt3 = "The rain in Spain"
xw = re.search("\s", txt3)

# 2. This will now successfully print: 3
print("The first white-space character is located in position:", xw.start())

print("..........If no matches are found, the value None is returned::............")

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
print(
    "..........The split() function returns a list where the string has been split at each match:............"
)
txt4 = "The rain in Spain"
xs = re.split("\s", txt4)
print(xs)

print("--------Split the string only at the first occurrence:-----------")
txt5 = "The rain in Spain"
xk = re.split("\s", txt5, 1)
print(xk)

print("-------------Replace every white-space character with the number 9:")
txt6 = "The rain in Spain"
xu = re.sub("\s", "9", txt6)
print(xu)
# You can control the number of replacements by specifying the count parameter:
print("-----------Replace the first 2 occurrences:-----------")
txt7 = "The rain in Spain"
xi = re.sub("\s", "9", txt7, 2)
print(xi)

print("...........Do a search that will return a Match Object:...............")
txt8 = "The rain in Spain"
xp = re.search("ai", txt8)
print(xp)  # this will print an object

print("Print the position (start- and end-position) of the first match occurrenceThe regular expression looks for any words that starts with an upper case S:")
txt9 = "The rain in Spain"
xl = re.search(r"\bS\w+", txt9)
print(xl.span())
print("---------Print the string passed into the function:--------")
txt10 = "The rain in Spain"
xg = re.search(r"\bS\w+", txt10)
print(xg.string)

print("The regular expression looks for any words that starts with an upper case S:")
txt11 = "The rain in Spain"
xd = re.search(r"\bS\w+", txt11)
print(xd.group())
