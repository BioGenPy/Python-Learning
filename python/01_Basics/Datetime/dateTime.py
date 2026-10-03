print("...........Python Datetime............")

import datetime

x = datetime.datetime.now()

print(f'Today date time is :\n {x}')

print(".........Return the year and name of weekday:.........")

t = datetime.datetime.now()
print(f"Current year : {t.year}")
print(f"week day is : {t.strftime("%A")}")

print("........Creating Date Objects.....................")

do = datetime.datetime(2026, 9, 28, 0)
print(do)

print("........Creating Date Objects : The strftime() Method .....................")

print(do.strftime("%B"))
