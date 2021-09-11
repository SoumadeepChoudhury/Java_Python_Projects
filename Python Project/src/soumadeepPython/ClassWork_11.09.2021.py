# # WAP to create a function in python that calculate area of the circle and return the value. Access the radius and call the above function.

def Area(r):
    area = 3.14*r*r
    return area


radius = int(input("Enter radius: "))
area = Area(radius)
print(f"The area of circle is : {area}")


# # WAP to find the sum of first n natural number using function.
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


user_Input = int(input("Enter value of n: "))
print(f"Sum of {user_Input} natural number is: {sum(user_Input)}")


# # Write a function to calculate the area of a rectangle.
def Area(l, b):
    area = l*b
    return area


length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
area = Area(length, breadth)
print(f"The area of rectangle is : {area}")


# # Define a function to calculate factorial of any number.
def factorial(n):
    f = 1
    if n == 0:
        return f
    else:
        for i in range(1, n+1):
            f *= i
        return f


user_Input = int(input("Enter any number to find factorial: "))
print(f"Factorial of {user_Input} is : {factorial(user_Input)}")


# # HOMEWORK  Suggested LAB Exercise. Q1,2,3
