# Accept a number a display 3 disgit from <n(n+1)(n+2)>.


n = int(input("Enter a number: "))
number = (n*100)+((n+1)*10)+(n+2)
print(number)
