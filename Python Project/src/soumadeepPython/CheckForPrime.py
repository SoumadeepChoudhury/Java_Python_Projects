# Check a number for prime....


a = int(input("Enter Number: "))
c = 0
for i in range(1, a+1):
    if a % i == 0:
        c += 1
if c == 2:
    print("Prime")
else:
    print("Not Prime")
