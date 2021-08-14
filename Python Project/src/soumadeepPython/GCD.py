# Find the GCD or HCF of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
n1, n2 = 0, 0
if a > b:
    n1 = a
    n2 = b
else:
    n1 = b
    n2 = a
x = 0
for i in range(1, n2+1):
    if n1 % i == 0 and n2 % i == 0:
        x = i

print("GCD: ", x)
