# # WAP accept a number and check whether it is 0ne digit/2/3 digit...
number = int(input("Enter number: "))
if(number > 999):
    print("More digit number.")
elif(number//100 != 0):
    print("3 digit number.")
elif(number//10 != 0):
    print("2 Digit number")
elif(number >= 0 and number < 10):
    print("1 digit number")


# # WAP print first 10 natural numbers.
for x in range(1, 11):
    print(x, end=",")


# # WAP print "GOOD MORNING" n times.
n = int(input("Enter n: "))
for i in range(0, n):
    print("GOOD MORNING")


# # WAP print all odd numbers from 10 to 100.
for i in range(10, 101):
    if(i % 2 != 0):
        print(i)
