# Check if two arrays contain same elemnets

list1, list2 = [], []

for i in range(0, 5):
    x = int(input("num: "))
    list1.append(x)
for i in range(0, 5):
    x = int(input("num 1 : "))
    list2.append(x)
list1.sort()
list2.sort()
f = -1
if (len(list1) != len(list2)):
    print("Not Equal")
else:
    for i in range(0, 5):
        if(list1[i] != list2[i]):
            print("Not Equal")
            f = 2
            break
    if f == -1:
        print("Equal")
