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
