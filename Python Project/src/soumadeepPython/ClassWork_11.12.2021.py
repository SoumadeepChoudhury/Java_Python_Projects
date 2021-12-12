# # WAP Input a welcome message and display it
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
