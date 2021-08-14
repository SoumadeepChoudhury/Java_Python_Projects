# Read three numbers and swap the first two variables with the sums of first & second, second & third respectively.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

a = a+b
b = b+c

print(a, b, c)
