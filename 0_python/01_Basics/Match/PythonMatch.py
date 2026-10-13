print(".................Python Match.......................................")

'''The Python Match Statement
Instead of writing many if..else statements, you can use the match statement.
The match statement selects one of many code blocks to be executed.'''

'''
Syntax
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
    
The match expression is evaluated once.
The value of the expression is compared with the values of each case.
If there is a match, the associated block of code is executed.
    
    
    '''

day = 5

#day = int(input("Pls Enter Your Day :  "))
match day :
  case 1 :
    print("Monday")
  case 2 :
    print("Tuesday")
    
  case 3 :
    print("Wednesday")
    
  case 4 :
    print("Thursday")
    
  case 5 :
    print("Friday")
    
  case 6 :
    print("Saturday")
  case 7 :
    print("Sunday")
  case _:
    print("Looking for Weekend")
print(".......................Combine Values..................")
'''Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case: '''

day = 7
match day :
  case 1 | 2 | 3 | 4 | 5  :
    print("Today is a Weekday")
    
  case 6 | 7 :
    print("I love Weekends ! ")

print(".......................If Statements as Guards..................")  
month = 5
day = 4
  
match day :
  
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A Weekday is April ")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A Weekday in May") 
  case _:
    print("No Match")
    