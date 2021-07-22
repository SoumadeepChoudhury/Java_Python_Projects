# Q.. WAP accept the value of a & b and display (a+b )^3.


# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# c = (a+b)**3
# print(c)


# Q...  WAP accept two numbers & display the remainder and quotient ..


# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# q = a//b
# r = a % b
# print("Quotient: ", q)
# print("Reminder: ", r)


# Q..  WAP accept two digit int no. & display its reverse.

# number = int(input("Enter number 1: "))
# d1 = number//10
# d2 = number % 10
# num_rev = (d2*10)+d1
# print(num_rev)


# Q... WAP accept three digit integer number display sum of digits

# number = int(input("Enter 3 digit number : "))
# d1 = number//100
# d = number % 100
# d2 = d//10
# d3 = d % 10
# sum = d1+d2+d3
# print(sum)


# Q.. WAP accept radius of a sphere & display its volume.

radius = float(input("Enter radius: "))
volume = 4/3*3.14*(radius**3)
print("Volume: ", volume)

# Q.. WAP accept the value of x,y,z & display the value of the expression x^3+x^2y^4+z^(3/2)


x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))
ex = (x**3)+((x**2)*(y**4))+(z**1.5)
print("Value of expression: ", ex)
