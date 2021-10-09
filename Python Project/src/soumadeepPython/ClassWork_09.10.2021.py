# # WAP accept 10 numbers in a tuple and find the sum of elements of tuple and display odd elements.

numbers = tuple()
odd = tuple()
for _ in range(10):
    num = int(input("Enter number: "))
    numbers += (num,)
print(sum(numbers))
for i in numbers:
    if(i % 2 != 0):
        odd += (i,)
print(odd)
