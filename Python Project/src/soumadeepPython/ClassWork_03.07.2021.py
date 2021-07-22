# # WAP display factors of a number.
num = int(input("Enter number: "))
i = 1
while(i <= num):
    if(num % i == 0):
        print(i, end=', ')
    i += 1


# # WAP in while loop to display first 5 even numbers.
x, n = 2, 0
while(n < 5):
    print(x)
    x += 2
    n += 1


# # WAP accept a number(<100) and display all numbers all the numbers.
n = int(input("Enter a number less than 100: "))
while(n <= 100):
    print(n)
    n += 1


# # WAP display first 10 odd number.
x, n = 1, 0
while(n < 10):
    print(x)
    x += 2
    n += 1


# # WAP display 10,9,8,7...1 using while loop.
n = 10
while(n > 0):
    print(n, end=', ')
    n -= 1
# # WAP display all even numbers between 500 to 1000
n = 502
while(n < 1000):
    print(n, end=', ')
    n += 2
