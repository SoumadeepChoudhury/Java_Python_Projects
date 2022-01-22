# WAP accept 10 elements in a list and display the perfect square elements in a list.
li = []
for _ in range(3):
    li.append(int(input("Enter value: ")))
for i in range(len(li)):
    if((li[i]**0.5) == int(li[i]**0.5)):
        print(li[i])
