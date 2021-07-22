# # WAP to build calculator..
num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))
op = input("Enter operator: ")
if(op == "+"):
    print(num1+num2)
elif(op == "-"):
    if(num1 > num2):
        print(num1-num2)
    else:
        print(num2-num1)
elif(op == "*"):
    print(num1*num2)
elif(op == '/'):
    if(num2 == 0):
        print("Error,Program terminated")
    else:
        print(num1/num2)
else:
    print("Wroung operator...")

# # Print each letter in A String
st = input("Enter String: ")
l = st[len(st)-1]
for letter in st:
    if(letter != l):
        print(letter, end='-')
    else:
        print(letter)


# # WAP print values in a list.
list = []
x = int(input("How many inputs u want? : "))
for i in range(0, x):
    list.append(input("Enter value: "))
for i in list:
    print(i)


# # Write a program that takes the name and age of the user as input and displays a message whether the user is eligible to apply for a driving license or not. (the eligible age is 18 years).
name = input("Enter name: ")
age = int(input("Enter age: "))
if(age >= 18):
    print("Eligible for driving license")
else:
    print("Not Eligible for driving license")


# # Write a function to print the table of a given number. The number has to be entered by the user.
def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")


number = int(input("Enter a number: "))
table(number)


# # Write a program that prints minimum and maximum of five numbers entered by the user.
list = []
for i in range(0, 5):
    list.append(int(input("Enter value: ")))
print(min(list))
print(max(list))
# OR
min = int(input("Enter a number: "))
max = min
for i in range(0, 4):
    x = int(input("Enter value: "))
    if(x > max):
        max = x
    elif(x < min):
        min = x
print(f"Max = {max}")
print(f"Min = {min}")


# # Write a program to check if the year entered by the user is a leap year or not.
year = int(input("Enter year in yyyy format: "))
if(year % 4 == 0 and year%100!=0 or year % 400 == 0):
    print("Leap Year")
else:
    print("Not a leap Year")
