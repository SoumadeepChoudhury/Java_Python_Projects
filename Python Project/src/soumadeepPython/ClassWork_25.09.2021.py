from random import randint
'''
Create a menu driven program using user defined
functions to implement a calculator that performs
the following:
    a) Basic arithmetic operations(+,-,*,/)
    b) log10(x),sin(x),cos(x)
'''
import math


def add(x, y):
    print(sum(x, y))


def subs(x, y):
    print(sum(x, -y))


def mult(x, y):
    print(math.prod(x, y))


def div(x, y):
    print(x / y)


def logarithm(x):
    print(math.log(x))


def sine(x):
    print(math.sin(x))


def cosine(x):
    print(math.cos(x))


print("1: Addition\n2: Substraction\n:3: Multiply\n4: Division\n5: Logarithm\n6: Sine value\n7: Cosine value.")
user_choice = int(input("Enter choice: "))
if(user_choice == 1):
    x = int(input("Enter 1st value: "))
    y = int(input("Enter 2nd value: "))
    add(x, y)
elif(user_choice == 2):
    x = int(input("Enter 1st value: "))
    y = int(input("Enter 2nd value: "))
    subs(x, y)
elif(user_choice == 3):
    x = int(input("Enter 1st value: "))
    y = int(input("Enter 2nd value: "))
    mult(x, y)
elif(user_choice == 4):
    x = int(input("Enter 1st value: "))
    y = int(input("Enter 2nd value: "))
    div(x, y)
elif(user_choice == 5):
    x = int(input("Enter 1st value: "))
    logarithm(x)
elif(user_choice == 6):
    x = int(input("Enter 1st value: "))
    sine(x)
elif(user_choice == 7):
    x = int(input("Enter 1st value: "))
    cosine(x)


# ########## HOMEWORK ######### #

# # To secure your account, whether it be an email, online bank account or any other account, it is important that we use authentication. Use your programming expertise to create a program using user defined function named login that accepts userid and password as parameters(login(uid, pwd)) that displays a message “account blocked” in case of three wrong attempts. The login is successful if the user enters user ID as "ADMIN" and password as "St0rE@1". On successful login, display a message “login successful”.
def login(uid, pwd):
    if(uid == "ADMIN" and pwd == "St0rE@1"):
        print("Login successful")
        return True


for checks in range(4):
    if(checks == 3):
        print("Account blocked")
        break
    print(f"Attempt {checks+1}")
    uid = input("Enter your ID: ")
    pwd = input("Enter Password: ")
    if(login(uid, pwd) == True):
        break
    elif(checks != 2):
        print("Try Again")


# # XYZ store plans to give festival discount to its customers. The store management has decided to give discount on the following criteria: Shopping Amount Discount Offered
# >=500 and <1000 5%
# >=1000 and <2000 8%
# >=2000 10%
# An additional discount of 5 % is given to customers who are the members of the store. Create a program using user defined function that accepts the shopping amount as a parameter and calculates discount and net amount payable on the basis of the following conditions: Net Payable Amount = Total Shopping Amount – Discount.
def discount(amt=0):
    dis = 0
    if(amt >= 500 and amt < 1000):
        dis = amt*5/100
    elif(amt >= 1000 and amt < 2000):
        dis = amt*8/100
    elif(amt >= 2000):
        dis = amt*10/100
    member_Check = input("Are you a member of the store? (Y/N): ").lower()
    if(member_Check == 'y'):
        dis += amt*5/100
    net_amt = amt-dis
    print(f"Your final payable amount is {net_amt}")


amount = float(input("Enter total shopping amount: "))
discount(amount)


# # ‘Play and learn’ strategy helps toddlers understand concepts in a fun way. Being a senior student you have taken responsibility to develop a program using user defined functions to help children master two and three-letter words using English alphabets and addition of single digit numbers. Make sure that you perform a careful analysis of the type of questions that can be included as per the age and curriculum.
print(".............PLAY & LEARN.............")


def addition_Play():
    number1 = randint(0, 9)             # Random module imported at top
    number2 = randint(0, 9)
    sum = int(input(f"What is the sum of {number1} and {number2} ? :\n"))
    if(sum == (number2+number1)):
        if(input("Congratulation...... Would you like to continue (Y/N) ?: \n").lower() == 'y'):
            addition_Play()
    else:
        if(input("Wrong answer... Wanna try Again ? (Y/N) ? ") == 'y'):
            addition_Play()
        else:
            print("Wrong Answer. ")


def TwoLetterWords():
    words = ["hi", "up", "on", "of", "to"]
    for i in words:
        choice = input(f"New Word: {i}\nWant to Continue (Y/N) ?: \n").lower()
        if(choice == 'n'):
            break


def ThreeLetterWords():
    words = ["hii", "hey", "top", "off", "too"]
    for i in words:
        choice = input(f"New Word: {i}\nWant to Continue (Y/N) ?: \n ").lower()
        if(choice == 'n'):
            break


user_Choice = int(input(
    "1.Sum of One Digit Number.\n2. Two letter words.\n3. Three Letter words."))
if(user_Choice == 1):
    addition_Play()
elif(user_Choice == 2):
    TwoLetterWords()
elif(user_Choice == 3):
    ThreeLetterWords()
