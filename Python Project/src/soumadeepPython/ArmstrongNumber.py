# Check a number for Amrstrong: 153 -> 1^3 +5^3 +3^3 == 153

class MyClass(object):
    num = int(input('Enter number: '))
    temp = num
    sum = 0
    while num > 0:
        digits = num % 10
        sum += digits*digits*digits
        num //= 10
    if(temp == sum):
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")
