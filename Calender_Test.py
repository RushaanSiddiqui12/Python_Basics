birth_date = int(input("Enter your Birth Date = "))
birth_month = input("Enter your Birth Month = ")
birth_year = int(input("Enter your Birth Year = "))

if(birth_year >= 2000 and birth_year<= 2099):
    y = 6

if(birth_month == "january"):
    x = 1
elif(birth_month == "february"):
    x = 4
elif(birth_month == "march"):
    x = 4
elif(birth_month == "april"):
    x = 0
elif(birth_month == "may"):
    x = 2
elif(birth_month == "june"):
    x = 5
elif(birth_month == "july"):
    x = 0
elif(birth_month == "august"):
    x = 3
elif(birth_month == "september"):
    x = 6
elif(birth_month == "october"):
    x = 1
elif(birth_month == "november"):
    x = 4 
elif(birth_month == "december"):
    x = 6

if(birth_year % 4 == 0):
    z = (birth_year -2000)//4
else:
    z = birth_year % 4
if(birth_month == "january"):
    x = 0
elif(birth_month == "february"):
    x = 3


test = (birth_date + x + y + z + (birth_year - 2000)) % 7
if(test == 0):
    a = "Saturday"
elif(test == 1):
    a = "Sunday"
elif(test == 2):
    a = "Monday"
elif(test == 3):
    a = "Tuesday"
elif(test == 4):
    a = "Wednesday"
elif(test == 5):
    a = "Thursday"
elif(test == 6):
    a = "Friday"

print("The day you were born was", a)
