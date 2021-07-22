# # 1
# # 1 2
# # 1 2 3
n = int(input("Enter value of n:"))
for i in range(0, n):
    for j in range(0, i+1):
        print(j+1, end=" ")
    print()


# # 1
# # 2 2
# # 3 3 3
n = int(input("Enter value of n:"))
for i in range(1, n+1):
    print((str(i)+' ')*i)


# # WAP print prime numbers fromm 2 to 50.
c = 0
for i in range(2, 51):
    c = 2
    for j in range(2, i):
        if(i % j == 0 and c < 3):
            c += 1
    if(c == 2):
        print(i, " is a prime no.")


# # Write a program to find the sum of digits of an integer number, input by the user.
n = int(input("Enter a integer number: "))
d, sum = 0, 0
while(n > 0):
    d = n % 10
    sum += d
    n //= 10
print(sum)


# # Write a function that checks whether an input number is a palindrome or not.
def palindrome_Checker(n):
    rev = ''.join(reversed(n))
    if(n == rev):
        print("Palindrome")
    else:
        print("Not Palindrome")


n = input("Enter a number: ")
palindrome_Checker(n)
