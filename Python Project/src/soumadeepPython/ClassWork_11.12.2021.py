# # WAP Input a welcome message and display it
from math import gcd, lcm
inp = input("Enter Welcome message: ")
print(inp)

# # Input two numbers and display the largest/smallest number.
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
print(max(num2, num1))
print(min(num2, num1))


# # Input three numbers and display the largest/smallest number.
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))
print(max(num2, num1, num3))
print(min(num2, num1, num3))


# # Give two integers x and n and compute x^n
x, n = int(input("Enter value of x: ")), int(input("Enter value of n: "))
print(x**n)


# # Find sum of series.
'''1+x+x^2+x^3+x^4....x^n'''
x = int(input("Enter value: "))
n = int(input("Enter power: "))
sum = 0
for i in range(0, n+1):
    sum += x**i
print(sum)


# # Find sum of series.
'''1-x+x^2-x^3+x^4....x^n'''
x = int(input("Enter value: "))
n = int(input("Enter power: "))
sum, k = 0, 1
for i in range(0, n+1):
    sum += (x**i)*k
    k *= -1
print(sum)


# # Find sum of series.
'''x+x^2/2-x^3/3+x^4/4...x^n/n'''
x = int(input("Enter value: "))
n = int(input("Enter power: "))
sum, k = x, 1
for i in range(2, n+1):
    sum += ((x**i)/i)*k
    k *= -1
print(sum)


# # Find sum of series.
'''x+x^2/2!-x^3/3!+x^4/4!...x^n/n!'''
x = int(input("Enter value: "))
n = int(input("Enter power: "))
sum, k = x, 1
for i in range(2, n+1):
    f = i
    for j in range(1, i):
        f *= i
    sum += ((x**i)/f)*k
    k *= -1
print(sum)


# # Determine whether a number is a perfect number,armstrong number or a palindrome number.
def perfect(number):
    sum = 0
    for i in range(1, number):
        if(number % i == 0):
            sum += i
        if(sum == number):
            return True
    return False


def armstrong(number):
    p, n, sum = len(str(number)), number, 0
    while (number > 0):
        d = number % 10
        sum += d**p
        number //= 10
    if(sum == n):
        return True
    return False


def palindrome(number):
    n, rev = number, 0
    while(number > 0):
        d = number % 10
        rev = rev*10+d
        number //= 10
    if(n == rev):
        return True
    return False


inp = int(input("Enter number: "))
if(perfect(inp)):
    print("Perfect Number: ")
elif(armstrong(inp)):
    print("Armstrong Number: ")
elif(palindrome(inp)):
    print("Palindrome Number: ")
else:
    print("None")


# # Input a number and check if the number is a prime or composite number.
inp = int(input("Enter a number: "))
c = 0
for i in range(1, inp+1):
    if(inp % i == 0):
        c += 1
if(c <= 2):
    print("Prime Number")
else:
    print("Composite Number")


# # Display the terms of a fibonacci series
n = int(input("Enter max limit or number of terms: "))
a, b, c = 0, 1, 0
print(a)
print(b)
for _ in range(3, n+1):
    c = a+b
    a, b = b, c
    print(c)


# # Compute the greatest common divisor and least common multiple of two intergers.
num1 = int(input("Enter Number1: "))
num2 = int(input("Enter Number2: "))
print(gcd(num1, num2))
print(lcm(num1, num2))


# # Count and display the number of vowels,consonants,uppercase,lowercase characters in string.
user_Inp = input("Enter String: ")
v, c, u, l = 0, 0, 0, 0
for i in user_Inp:
    if(i.isupper()):
        u += 1
    if(i.islower()):
        l += 1
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        v += 1
    elif(i.isdigit() == False):
        c += 1
print(f"Vowels = {v}")
print(f"Consonants = {c}")
print(f"Uppercase = {u}")
print(f"Lowercase = {l}")


# # Input a String and determine whether it is a palindrome or not; convert the case of characters in a string.
inp = input("Enter a String: ")
if(inp == reversed(inp)):
    print("Palindrome")
else:
    print("Not Palindrome")
print(inp.swapcase())


# # Find the largest/smallest number in a list/tuple
li_tu = eval(input("Enter a list or a tuple: "))
print(f"Max is {max(li_tu)}")
print(f"Min is {min(li_tu)}")


# # Input a list of numbers and swap elements at the even location with elements at the odd location.
li = eval(input("Enter a list of numbers: "))
for i in range(0, len(li)+1, 2):
    if(i < len(li) and len(li) % 2 == 0):
        li[i], li[i+1] = li[i+1], li[i]
    elif(len(li) % 2 != 0 and i < len(li)-1):
        li[i], li[i+1] = li[i+1], li[i]
print(li)


# # Input a list/tuple of elements, search for a given element in list/tuple.
li = eval(input("Enter list/Tuple: "))
search = input("Enter Search value")
search = int(search) if search.isdigit else search
if search in li:
    print(li.index(search))


# # Input a list of numbers and test if a number is equal to the sum of cubes of the digits. Find the smallest and largest such number from the given list of numbers.
li = eval(input("Enter list of numbers: "))
lx = []
for i in li:
    x, sum = i, 0
    while x > 0:
        d = x % 10
        sum += d**3
        x //= 10
    if(i == sum):
        print(f"{i} has Equal")
        lx.append(i)
print("Largest is", max(lx))
print("Smallest is", min(lx))


# # Create a dictionary with roll no,name,marks of n students in a class asn display the names of the students who have marks above 75.
class Student():
    def students():
        d, d1 = {}, {}
        n = int(input("Enter no of students: "))
        for i in range(0, n):
            d1 = {}
            rollno = int(input("Enter Roll Number"))
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            d1['rollno'], d1['marks'] = rollno, marks
            d[name] = d1
        print(d)
        for i in list(d.keys()):
            if(d[i]['marks'] > 75):
                print(f"{i} has scored above 75")


print(Student.students())
