# WAP accept 10 elements in a list and display the perfect square elements in a list.
from math import pow
li = []
for _ in range(10):
    li.append(int(input("Enter value: ")))
for i in range(len(li)):
    if(pow(li[i], 0.5) == int(pow(li[i], 0.5))):
        print(li[i])
