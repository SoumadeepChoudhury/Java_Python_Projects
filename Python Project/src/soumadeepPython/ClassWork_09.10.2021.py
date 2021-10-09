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


# # Write a program to read email IDs of n number of students and store them in a tuple. Create two new tuples, one to store only the usernames from the email IDs and second to store domain names from the email ids. Print all three tuples at the end of the program.


# # Write a program to input names of n students and store them in a tuple. Also, input a name from the user and find if this student is present in the tuple or not.
names = tuple()
n = int(input("How many names would you like to enter? "))
for _ in range(n):
    names += (input("Enter name: "),)
name_Check = input("Enter name to check within list: ")
if(name_Check in names):
    print("Name found in tuple")
else:
    print("Name not found in tuple")
