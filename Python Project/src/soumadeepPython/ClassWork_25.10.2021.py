# # Print the series 1,-4,7,-10....-40
k = 1
for i in range(1, 41, 3):
    print(i*k, end=" ")
    k *= -1


# # WAP accept a sentence and display a word formed by each first letter of the sentence.
userInp = input("Enter a sentence: ").strip()
newWord = userInp[0]
for i in range(0, len(userInp)):
    if userInp[i] == " ":
        newWord += userInp[i+1]
print(newWord)


# # Assign in tuples.
tup = tuple()
for _ in range(10):
    userInp = int(input("Enter value: "))
    tup += (userInp,)
print(tup)


# # WAP accept name roll no and marks of 10 students in nested tuple and display them in tabular format.
studDetail = tuple()
for _ in range(10):
    rollNo = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    studDetail += ((rollNo, name, marks),)
print("S_No", " Roll_No", " Name", " Marks")
for i in range(0, len(studDetail)):
    print((i+1), '\t', studDetail[i][0], '\t',
          studDetail[i][1], '\t', studDetail[i][2])


################# HOMEWORK #########################
# # Write a Python program that creates a tuple storing first nine terms of  a Fibonacci series.
term1, term2 = 0, 1
fib_series = (term1, term2)
for _ in range(7):
    term3 = term1+term2
    fib_series += (term3,)
    term1, term2 = term2, term3
print(fib_series)


# # a) Write a program that receives the index and returns the corresponding value.
user_Index = int(input("Enter Index: "))
print(fib_series[user_Index] if (
    user_Index < len(fib_series)) else "Not Found")

# b) Write a program that receives a fibonacci term and returns a number telling which term it is. For instance, if you pass 3, it returns 5, telling it is 5th term, for 8, returns 7
user_Inp = int(input("Enter a fibonacci term: "))
print(fib_series.index(user_Index),
      "th term" if(user_Inp in fib_series) else "Not Found")


# # Write a program to input n numbers from the user store these numbers in a tuple. Print the maximum and minimum number from this tuple.
user_Data = tuple()
while(True):
    user_Data += (int(input("Enter value: ")),)
    if(input("Do you wnat to continue (Y/N)? ").lower() == 'n'):
        break
print(max(user_Data))
print(min(user_Data))


# # Write a program to create a nested tuple to store role number, name and marks of the students.
students = tuple()
while True:
    roll, name, marks = int(input("Enter Roll No: ")
                            ), input("Enter name: "), float(input("Enter marks: "))
    students += ((roll, name, marks),)
    if(input("Wanna Add More (Y/N)? ").lower() == 'n'):
        break


# # Write a program that interactively creates a nested tuple to store the marks in three subjects for five students.
students = tuple()
for _ in range(5):
    marks1, marks2, marks3 = int(input("Enter marks1: ")
                                 ), input("Enter marks2: "), float(input("Enter marks3: "))
    students += ((marks1, marks2, marks3),)
