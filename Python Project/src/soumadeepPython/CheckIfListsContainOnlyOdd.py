# Check If lists Contain Only Odd Numbers.........

l = []
num = int(input("Enter length: "))
for i in range(num):
    data = int(input())
    l.append(data)
c = 0
for i in range(num):
    if(l[i] % 2 == 0):
        print("Doesn't Contain Only Odd Numbers...")
        break
    else:
        c += 1
if(c == num):
    print("Contains Only Odd Numbers")
