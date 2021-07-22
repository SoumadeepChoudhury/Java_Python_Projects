# Print the Fibonacci Series

a, b, c = 0, 1, 0
print(a, ",", b, end=", ")
for i in range(3, 10):
    c = a+b
    print(c, end=", ")
    a = b
    b = c
print()
