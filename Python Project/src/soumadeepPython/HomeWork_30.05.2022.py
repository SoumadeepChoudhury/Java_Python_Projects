# WAP to count the words "to" and "the" present in a text file "Poem.txt".
count_to = 0
count_the = 0
with open("Poem.txt") as file:
    for lines in file:
        for words in lines.split():
            if words == "to":
                count_to += 1
            elif words == "the":
                count_the += 1
print(f"No. of 'to' is {count_to}")
print(f"No. of 'the' is {count_the}")


# Write a function AMCount() in python, which should read each character of a text file STORY.TXT, should count and display the occurence of alphabets A and M (including small cases a and m too).
def AMCount():
    count_a = 0
    count_m = 0
    with open("STORY.TXT") as file:
        for lines in file:
            for words in lines.split():
                for char in words.lower():
                    if char == "a":
                        count_a += 1
                    elif char == "m":
                        count_m += 1
    print(f"No. of 'a' is {count_a}")
    print(f"No. of 'm' is {count_m}")


# Write a function in Python to count and display the number of lines starting with alphabet 'A' present in a text file " LINES.TXT"
def Counter():
    count = 0
    with open("LINES.TXT") as file:
        for lines in file:
            if lines.startswith("A"):
                count += 1
    print(f"No. of lines strting with 'A': {count}")


# Write a program that counts the number of characters up to the first $ in a text file.
file = open("file.txt").read()
charcount = file.index('$')
print(charcount)

# Write a program that counts the number alphabets and digits of characters up to the first $ in a text file.
countalpha, countdigit = 0, 0
file = open("file.txt").read()
if '$' in file:
    substring = file[:file.index('$')]
    for i in substring:
        if i.isalpha():
            countalpha += 1
        elif i.isdigit():
            countdigit += 1
else:
    print("$ Not Found")
print(f"No. of digits: {countdigit}")
print(f"No. of alphabets: {countalpha}")

# Updated in another style
file = open("file.txt").read()
c1, c2, c = 0, 0, 0
for i in file:
    if i == '$':
        break
    elif(i.isalpha()):
        c1 += 1
    elif(i.isdigit()):
        c2 += 1
print("Alpha: ", c1)
print("Digit: ", c2)

# Write a program that will create an object called filout for writing, associate it with the filename STRS.txt. The code should keep on writing strings to it as long as the user wants.
while True:
    with open("STRS.txt", "a") as filout:
        userInput = input("Enter String or 0 to discontinue: ")
        if userInput == 0:
            break
        filout.write(userInput)


# Write a function Show_words() in python to read the content of a text file ‘NOTES.TXT’ and display only such lines of the file which have exactly 5 words in them.
def Show_words():
    file = open("NOTES.TXT")
    line = True
    while line:
        line = file.readline()
        if len(line.split()) == 5:
            print(line)


# WAP that copies one file to another. Have the program read the file names from user.
userFromFile = input("Enter file name to be copied: ").removesuffix(".txt")
userToFile = input(
    "Enter new file name where to be copied: ").removesuffix(".txt")
with open(f"{userFromFile}.txt") as f:
    with open(f"{userToFile}.txt", "w") as f1:
        for line in f:
            f1.write(line)


# WAP that appends the contents of one file to another. Have the program read the file names from user.
userFromFile = input("Enter file name to be copied: ").removesuffix(".txt")
userToFile = input(
    "Enter new file name where to be copied: ").removesuffix(".txt")
with open(f"{userFromFile}.txt") as f:
    with open(f"{userToFile}.txt", "a") as f1:
        for line in f:
            f1.write(line)


# Write a program that reads characters from the keyboard one by one. All lower case characters get stored inside the file LOWER, all upper case characters get stored inside the file UPPER and all other characters get stored inside file OTHERS.
lowerFile = open("LOWER.txt", "a")
upperFile = open("UPPER.txt", "a")
othersFile = open("OTHERS.txt", "a")
while True:
    userChar = input("Enter one character: ")[0]
    if userChar.isupper():
        upperFile.write(userChar)
    elif userChar.islower():
        lowerFile.write(userChar)
    else:
        othersFile.write(userChar)
