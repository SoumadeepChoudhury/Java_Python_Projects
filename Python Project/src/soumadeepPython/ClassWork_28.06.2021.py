# # WAP accept n numbers and display all natural no. upto n.
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i)


# # WAP accept a number and display all even nunbers from 1 to that no.
n = int(input("Enter number: "))+1
for i in range(1, n):
    if(i % 2 == 0):
        print(i)


# # WAP display the series: -1,-3,-5,-7,-9,-11
for i in range(-1, -12, -2):
    print(i, end=' ')


# # Write a program to generate the sequence: –5, 10,–15, 20, –25….. upto n, where n is an integer input by the user.
n = int(input("Enter value of n: "))
k = -1
for i in range(5, n+1, 5):
    print(i*k, end=", ")
    k *= -1


# # Write a program to find the sum of 1+ 1/8 +1/27......1/n^3, where n is the number input by the user.
n = int(input("Enter number: "))
sum = 0
for i in range(1, n+1):
    sum += (1/i**3)
print(sum)


# # Write a program to find the sum of digits of an integer number, input by the user.
num = int(input("Enter number: "))
sum = 0
while(num > 0):
    d = num % 10
    sum += d
    num //= 10
print("Sum: ", sum)


# # Write a program to find the grade of a student when grades are allocated as given in the table below.Percentage of the marks obtained by the student is input to the program.
# Percentage of Marks Grade
# Above 90 % A
# 80 % to 90 % B
# 70 % to 80 % C
# 60 % to 70 % D
# Below 60 % E
percent = float(input("Enter percentage: "))
if(percent >= 90):
    print("Grade: A")
elif(percent >= 80 and percent < 90):
    print("Grade: B")
elif(percent >= 70 and percent < 80):
    print("Grade: C")
elif(percent >= 60 and percent < 70):
    print("Grade: D")
else:
    print("Grade: E")
