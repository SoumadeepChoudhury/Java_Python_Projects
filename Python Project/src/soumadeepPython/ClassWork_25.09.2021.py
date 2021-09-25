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
