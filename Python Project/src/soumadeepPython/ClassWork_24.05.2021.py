# # WAP accept amount in Rs. And display how many 100 notes 50 notes 20 notes , 10 note,5,2,1 note in that amount.

amount = int(input("Enter amount: "))
c100, c50, c20, c10, c5, c2, c1 = 0, 0, 0, 0, 0, 0, 0

if(amount >= 100):
    c100 = amount//100
    amount = amount-(c100*100)
if(amount >= 50):
    c50 = amount//50
    amount -= (c50*50)
if(amount >= 20):
    c20 = amount//20
    amount -= (c20*20)
if(amount >= 10):
    c10 = amount//10
    amount -= (c10*10)
if(amount >= 5):
    c5 = amount//5
    amount -= (c5*5)
if(amount >= 2):
    c2 = amount//2
    amount -= (c2*2)
if(amount >= 1):
    c1 = amount//1
    amount -= (c1*1)


print("No of Notes for Rs.100", c100)
print("No of Notes for Rs.50", c50)
print("No of Notes for Rs.20", c20)
print("No of Notes for Rs.10", c10)
print("No of Notes for Rs.5", c5)
print("No of Notes for Rs.2", c2)
print("No of Notes for Rs.1", c1)

# # # # OR


c100 = amount//100
amount = amount % 100

c50 = amount//50
amount = amount % 50

c20 = amount//20
amount = amount % 20

c10 = amount//10
amount = amount % 10

c5 = amount//5
amount = amount % 5

c2 = amount//2
amount = amount % 2

c1 = amount//1
amount = amount % 1

print("No of Notes for Rs.100", c100)
print("No of Notes for Rs.50", c50)
print("No of Notes for Rs.20", c20)
print("No of Notes for Rs.10", c10)
print("No of Notes for Rs.5", c5)
print("No of Notes for Rs.2", c2)
print("No of Notes for Rs.1", c1)


# # WAP accept a float type no. and display it's integer part& float part.

n = float(input("Enter number: "))
print("Integer: ", int(n))
print("Float: ", (n-int(n)))


# # WAP accept three side and check whether forming triangle or not and display area

s1 = float(input("Enter side1: "))
s2 = float(input("Enter side2: "))
s3 = float(input("Enter side3: "))
s, area = 0, 0
if((s1+s2) > s3 or (s1+s3) > s2 or (s3+s2) > s1):
    print("Forms triangle")
    s = (s1+s2+s3)/2
    area = (s*(s-s1)*(s-s2)*(s-s3))**(0.5)
    print("Area: ", area)
else:
    print("Do not form triangle")


# # WAP accept three side of triangle and check whether right-angled triangle and display area & if not formed then display area...

b = float(input("Enter side1: "))
h = float(input("Enter side 2: "))
p = float(input("Enter side3: "))
s = (b+p+h)/2
area = (s*(s-b)*(s-p)*(s-h))**0.5
if((b+p) > h or (b+h) > p or (p+h) > b):
    if((b**2 + p**2) == h**2 or (b**2 + h**2) == p**2 or (p**2 + h**2) == b**2):
        print("Right angled triangle")
        print("Area: ", area)
    else:
        print("Do not form right angled triangle")
        print("Area: ", area)
else:
    print("Do not form Triangle")


# # WAP accept the coeff. of x^2 and x and a contant value of a equation and display roots.


a = int(input("Enter coefficient of x^2: "))
b = int(input("Enter coefficient of x: "))
c = int(input("Enter contant term: "))
D = (b**2)-(4*a*c)
root1, root2 = 0, 0
if(D > 0):
    root1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
    root2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
    print("Root 1 : ", root1)
    print("Root 2 : ", root2)
elif(D == 0):
    root1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
    root2 = root1
    print("Root 1 : ", root1)
    print("Root 2 : ", root2)
else:
    print("Form Complex root.")
