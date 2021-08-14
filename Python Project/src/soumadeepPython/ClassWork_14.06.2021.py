# # WAP accept a number and check whether + or -

number = int(input("Enter number: "))
if(number > 0):
    print("Positive number")
elif(number < 0):
    print("Negative number")
else:
    print("Zero")


# # WAP accept a number & check whether 3 digit or not.

num = int(input("Enter number: "))
if(num//100 != 0):
    print("3 digit number")
else:
    print("Not 3 digit number")

# # WAP accept age of a people & check whether s/he is senior citizon or not.(>=60)
age = int(input("Enter age: "))
if(age >= 60):
    print("Senior citizen")
else:
    print("Not Senior citizen")

# # WAP accept age of a person & check whether he is eligible for COVID vaccine or not.(>=18)
age = int(input("Enter age: "))
if(age >= 18):
    print("Eligible for COVID vaccine")
else:
    print("Not Eligible for COVID vaccine")
