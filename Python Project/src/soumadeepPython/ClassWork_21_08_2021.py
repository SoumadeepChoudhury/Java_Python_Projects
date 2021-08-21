# # WAP accept two numbers amd display the GCD and LCM.
import math
number1 = int(input("Enter Number: "))
number2 = int(input("Enter Number: "))
print("LCM: ", math.lcm(number1, number2))  # For Python 3.9+
print("GCD: ", math.gcd(number1, number2))


# # WAP to read a list of n integer (+ or - ). Create two new list one having all positive number and other having all negative number. Print all three lists.

list1, list2, list3 = [], [], []
n = int(input("How many numbers you wanna input? : "))
for _ in range(n):
    input_Number = int(input("Enter the value: "))
    list1.append(input_Number)
for i in list1:
    if(i > 0):
        list2.append(i)
    elif(i < 0):
        list3.append(i)
print(list1)
print(list2)
print(list3)
