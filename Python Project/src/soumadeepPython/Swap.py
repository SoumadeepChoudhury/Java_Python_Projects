# Swap Two Numbers without third Variable...

a = (int(input("Enter number in a : ")))
b = (int(input("Enter number in b: ")))
a = a*b  # a=a+b
b = a//b  # b=a-b
a = a//b  # a=a-b
print("After Swaping")
print("Value of a: ", a, "\nValue of b: ", b)
