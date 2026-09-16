name = "kamalesh"
# print ("k" in name)  # True
# print ("z" in name)  # False

# ============= true
name = " programming"
# print ("python" not   in name)   # True


# =============2. Membership with Lists
language = ["python", "java", "c++", "javascript"]
# print ("python" in language)  # True
# print ("ruby" in language)  # False

# =============3. Membership with Tuples
language = ("python", "java", "c++", "javascript")
# print ("python" in language)  # True
# print ("ruby" in language)  # False

#==================4. Membership with Dictionaries
numbers = (1, 2, 3, 4, 5 )
# print (1 in numbers)  # True

# ================== 4. Membership with Dictionaries

students = {
  
  "name": "kamalesh",
  "age": 25,
  "city": "Bangalore"
}
# print ("name" in students)  # True

# =============== Real Job Example
# valid_roles = ["admin", "user", "manager"]
# role = input("Enter your role: ").strip().lower()

# if role in valid_roles:
#     print("Access granted.")
# else:
#     print("Invalid role.")

# How do you check dictionary values?
students = {
    "name": "kamalesh",
    "age": 25,
    "city": "Bangalore"
}
# print ("kamalesh" in students.values())  

# ------------ Ask the user for a letter. Exercise 1
#--------------------Ask the user for a letter.
words = ["python"]
letter = input("Enter a letter: ").strip().lower()
if letter in words[0]:
    print(f"The letter '{letter}' is present in the word '{words[0]}'.")
else:
    print(f"The letter '{letter}' is not present in the word '{words[0]}'.")  
# -------------------  Exercise 2   Ask the user for a fruit.
fruits = ["apple", "banana", "orange"]
fruit = input("Enter a fruit: ").strip().lower()
if fruit in fruits:
    print(f"The fruit '{fruit}' is available.")
else:
    print(f"The fruit '{fruit}' is not available.")
    
# --------------------- Exercise 3 :  Ask the user for a country.
countries = ["India", "USA", "Canada", "Australia"]
country = input("Enter a country: ").strip().title()  
if country in countries:
    print(f"The country '{country}' Country not supported.")
else:
    print(f"The country '{country}' Country not supported.")

# --------------------- Exercise 4 : Ask the user for a key.
students = {
    "name": "kamalesh",
    "age": 25,
    "city": "Bangalore"
}
key = input("Enter a key: ").strip()
if key in students:
    print(f"Key Found'{key}'")
else:
    print(f"Key  '{key}'  Not Found.")
    
# --------------------- Exercise 5 : Ask the user for a value.
students = {  
    "name": "kamalesh",
    "age": 25,
    "city": "Bangalore"
}
value = input("Enter a value: ").strip()
if value in students.values():
    print(f"Value Found'{value}'")
else:
    print(f"Value  '{value}'  Not Found.")

# --------------------- Exercise 6 : Create a list of programming languages.Ask the user to enter one.Tell them whether it is supported.
programming_languages = ["python", "java", "c++", "javascript"]
language = input("Enter a programming language: ").strip().lower()
if language in programming_languages:
    print(f"The programming language '{language}' is supported.")
else:
    print(f"The programming language '{language}' is not supported.")
    
# --------------------- Exercise 7 : Password Validator  ,Allowed passwords:
allowed_passwords = [
    "python123",
    "admin123",
    "welcome123"
]
password = input("Enter your password: ").strip()
if password in allowed_passwords:
    print("Login Successful.")
else:
    print("Invalid Password.")
    
# --------------------- Exercise 8 : Movie Search 
movies = [
    "Inception",
    "Interstellar",
    "Avatar",
    "Titanic"]
movie = input("Enter a movie name: ").strip()
if movie in movies:
    print(f"The movie '{movie}' is available.")
else:
    print(f"The movie '{movie}' is not available.")

# --------------------- Exercise 9 : Create a menu.
menu = [
    "1. View Products",
    "2. Add Product",
    "3. Remove Product",
    "4. Exit"
]
print("Menu:")
for item in menu:
    print(item)

# --------------------- Exercise 10 : Create a dictionary:Ask the user for an employee ID.Tell them whether the ID exists.

employees = {
    "001": "kamalesh",
    "002": "subrata",
    "003": "ratan"
}
employee_id = input("Enter an employee ID: ").strip()
if employee_id in employees:
    print(f"Employee found: {employees[employee_id]}")
else:
    print("Employee not found.")