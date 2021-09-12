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


####################### HOMEWORK ###########################


# # Write a program to check the divisibility of a number by 7 that is passed as a parameter to the user defined function.
def check_Divisiblity(n):
    if(n % 7 == 0):
        return "Divisible"
    else:
        return "Indivisible"


user_Input = int(input("Enter Number: "))
print(f"{user_Input} is {check_Divisiblity(user_Input)} by 7")


# # Write a program that uses a user defined function that accepts name and gender(as M for Male, F for Female) and prefixes Mr/Ms on the basis of the gender.
def prefixes(name, gender):
    if(gender == 'M'):
        name = "Mr. "+name
    elif(gender == 'F'):
        name = "Ms. "+name
    else:
        return "Type your gender correctly"
    return name


name = input("Enter your Name: ")
gender = input(
    "Enter your Gender as 'M' for Male and 'F' for Female: ").upper()
print(prefixes(name, gender))


# # Write a program that has a user defined function to accept the coefficients of a quadratic equation in variables and calculates its determinant. For example: if the coefficients are stored in the variables a, b, c then calculate determinant as b^2-4ac. Write the appropriate condition to check determinants on positive, zero and negative and output appropriate result.
def quadratic_Solver(a, b, c):
    determinant = (b**2) - (4*a*c)
    return determinant


a = int(input("Enter coefficient of x^2: "))
b = int(input("Enter coefficient of x: "))
c = int(input("Enter constant term: "))
print(f"The result of the quadratic equation is {quadratic_Solver(a,b,c)}")
