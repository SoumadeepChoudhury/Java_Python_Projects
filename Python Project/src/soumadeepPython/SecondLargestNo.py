# Find the second largest no in an array

li = []
for i in range(0, 5):
    li.append(int(input("Enter num: ")))

li.sort(reverse=True)
print(li[1])
