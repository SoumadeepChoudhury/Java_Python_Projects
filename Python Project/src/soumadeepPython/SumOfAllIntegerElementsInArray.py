# Sum of all integer elements in array


li1 = []
sum = 0
for i in range(0, 5):
    x = int(input("Enter value: "))
    li1.append(x)
    sum += li1[i]
print(sum)
