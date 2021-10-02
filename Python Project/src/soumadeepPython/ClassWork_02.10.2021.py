# # Create a function to convert Fahrenheit to Celsius & Vice versa.

def temperature(value, unit):
    conv = 0
    if(unit == 'F'):
        conv = (value-32)*5/9
        unit = 'C'
    else:
        conv = (value*9/5)+32
        unit = 'F'
    print(f"The required temp is {conv} {unit}")


temp = input(
    "Enter temperature in F/C scale (eg: 98 F or 38 C etc): ").upper().strip()
unit = temp[-1]
value = int(temp[:len(temp)-1])
temperature(value, unit)


# # 1,2,8
############### HOMEWORK #############
'''
Q1

Consider the following tuples, tuple1 and tuple2:
tuple1 = (23, 1, 45, 67, 45, 9, 55, 45)
tuple2 = (100, 200)
Find the output of the following statements:
    i. print(tuple1.index(45))      # 2
    ii. print(tuple1.count(45))     # 3
    iii. print(tuple1 + tuple2)     # (23, 1, 45, 67, 45, 9, 55, 45,100, 200)
    iv. print(len(tuple2))      # 2
    v. print(max(tuple1))       # 67
    vi print(min(tuple1))       # 1
    vii. print(sum(tuple2))         # 300
    viii. print(sorted(tuple1))         
    print(tuple1)                   # (1,9,23,45,45,45,55,67)
'''
