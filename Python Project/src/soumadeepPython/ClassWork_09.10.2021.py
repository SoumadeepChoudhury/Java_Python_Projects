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
email = tuple()
usernames = tuple()
domain = tuple()
n = int(input("How many email IDs would you like to enter: "))
for i in range(n):
    email += (input("Enter email ID: "),)
    usernames += (email[i].split('@')[0],)
    domain += (email[i].split('@')[1],)
print(email)
print(usernames)
print(domain)


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


################################ HOMEWORK ##########################
'''Write a program to take in the roll number, name and percentage of marks for n students of Class X. Write user defined functions to
    • accept details of the n students(n is the number of students)
    • search details of a particular student on the basis of roll number and display result
    • display the result of all the students
    • find the topper amongst them'''
name = list()
roll = list()
percent = list()


def accept_details():
    for _ in range(int(input("How many student's details you wanna enter ? "))):
        name.append(input("Enter Student name: "))
        roll.append(int(input("Enter Roll No: ")))
        percent.append(float(input("Enter percent: ")))


def search_details(roll_No):
    index = 0
    for i in range(len(roll)):
        if roll[i] == roll_No:
            index = i
    print(
        f"Name of Student having roll no {roll_No}: {name[index]} has the percentage {percent[index]}")


def display_results():
    for i in range(len(name)):
        print(f"Name: {name[i]} Roll No: {roll[i]} Percent: {percent[i]}")


def topper_find():
    topper = percent[0]
    index = 0
    for i in range(1, len(percent)):
        if(topper < percent[i]):
            topper = percent[i]
            index = i
    print(
        f"The topper is {name[index]} bearing Roll No: {roll[index]} having percentage: {percent[index]}")


print("First fill up the details of the student of your Class X ...")
accept_details()

userChoice = int(input(
    "1. Wanna search particular student details ?\n2. Wanna display all the students result ?\n3. Wanna find the topper amoung them ?\n4.Exit.\nEnter 1,2,3,4..  "))
if(userChoice == 1):
    rollNO = int(input("Enter Roll No of the Student: "))
    search_details(rollNO)
elif(userChoice == 2):
    display_results()
elif(userChoice == 3):
    topper_find()
else:
    exit()
