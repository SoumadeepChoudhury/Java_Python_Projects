# # Q .. Write a Python program to calculate the amount payable if money has been lent on simple interest. Principal or money lent = P, Rate = R% per annum and Time = T years. Then Simple Interest (SI) = (P x R x T)/ 100.
# Amount payable = Principal + SI.
# P, R and T are given as input to the program.

from datetime import date
P = float(input("Enter principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
S_I = (P*R*T)/100
Amount = P+S_I
print("Amount Payable: ", Amount)

# ````````````````````````````````````````````````````````````````````````````````````````````````````


# # Q... Write a program to repeat the string ‘‘GOOD MORNING” n times. Here n is an integer entered by the user.


n = int(input("No. of times you wanna repeat: "))
for i in range(0, n):
    print("GOOD MORNING")


# ``````````````````````````````````````````````````````````````````````````````````````````````````````

# # Q.. Write a program to find the average of 3 numbers.

n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))
n3 = int(input("Enter num3: "))
print((n1+n2+n3)/3)


# ````````````````````````````````````````````````````````````````````````````````````````````````````

# # Q.. Write a program that asks the user to enter one's name and age. Print out a message addressed to the user that tells the user the year in which he/she will turn 100 years old.
name = input("Enter name: ")
age = int(input("Enter age: "))
remaining_age = 100-age
year_required = date.today().year + remaining_age
print("Dear "+name+" you will age 100 years old in the year ", year_required)
