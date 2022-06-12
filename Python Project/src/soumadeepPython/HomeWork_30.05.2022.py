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


################ BINARY FILES ################


# A file sports.dat contains information in following format : Event ~ Participant. Write a function that would read contents from file sports.dat and creates a file named Atheletic.dat copying only those records from sports.dat where the event name is “Atheletics”.
import pickle
def ReadWriteDat():
    sportsFile = open("sports.dat", "rb")
    try:
        with open("Atheletic.dat","wb") as newFile:
            while True:
                lines = pickle.load(sportsFile)
                if lines["Event"] == "Atheletics":
                    pickle.dump(lines,newFile)
    except EOFError:
        sportsFile.close()


# A file contains a list of telephone numbers in the following form:
#                           Arvind 7258031
#                           Sachin 7259197
# The names contain only one word the names and telephone numbers are separated by white spaces Write program to read a file and display its contents in two columns.
telephoneFile = open("telephone.txt", "r")
line = " "
while line:
    line = telephoneFile.readline().split()
    try:
        if line[0] != "" or line != " ":
            print(line[0]+'|'+line[1])
    except:
        break


# Consider the following definition of dictionary Member, write a method in python to write the content in a pickled file member.dat.
#                       Member = {'MemberNo.': _____, 'Name': _____}
import pickle
def Members():
    Member={'MemberNo':1,'Name':"BB Roy"}
    with open("member.dat","wb") as member:
        pickle.dump(Member,member)


# Consider the following definition of dictionary Staff, write a method in python to search and display the content in a pickled file staff.dat, where Staffcode key of the dictionary is matching with 'S0105'
#                          Staff = {'Staffcode":_____ 'Name' = _________}
import pickle
def Staffs():
    staffsFile = open("staff.dat", "rb")
    try:
        while True:
            Staff = pickle.load(staffsFile)
            if Staff['Staffcode']=='S0105':
                print(f"Name of the staff having code S0105 is {Staff['Name']}")
    except EOFError:
        staffsFile.close()


# Considering the following definition of dictionary COMPANY, Write a method in Python to search and display the content in a pickled file COMPANY.DAT, where CompID key of the dictionary is matching with the value '1005'.
#                       Company = {'CompID' = ____, 'CName' = ____, ‘Turnover’ = ____}
import pickle
def Companys():
    companyFile = open("COMAPNY.DAT", "rb")
    try:
        while True:
            Company = pickle.load(companyFile)
            if Company['ComID']=='1005':
                print(f"CName : {Company['CName']}\nTurnover : {Company['Turnover']}")
    except EOFError:
        companyFile.close()



########################### CSV Files #############################

# WAP to read a given CSV file having tab delimiter.
import csv
file=open('file.csv','r',newline='')
reader=csv.reader(file,delimiter='\t')
for rec in reader:
    print(rec)



# Write a Python program to write a nested Python list to a csv file in one go. After writing the CSV read the CSV file and display the content.
import csv
lst=eval(input("Enter a nested list: "))
with open("file.csv",'w',newline='') as csvf:
    writer=csv.writer(csvf)
    writer.writerows(lst)

with open("file.csv","r",newline='') as cvf:
    reader=csv.reader(cvf)
    for rec in reader:
        print(rec)


# Write a function that reads a csv file and creates another csv file with the same content, but with a different delimeter.
def Transformer():
    import csv
    lst=[]
    with open("file1.csv","r",newline='') as cnf:
        reader=csv.reader(cnf)
        for i in reader:
            lst.append(i)
    with open("file2.csv","w",newline='') as cnf:
        writer=csv.writer(cnf,delimiter='|')
        writer.writerows(lst)


# Write a function that reads a csv file and creates another csv file with the same content except the lines begining with 'check'.
def TransformerRepeater():
    import csv
    lst=[]
    with open("file1.csv","r",newline='') as cnf:
        reader=csv.reader(cnf)
        for i in reader:
            lst.append(i)
    with open("file2.csv","w",newline='') as cnf:
        writer=csv.writer(cnf,delimiter='|')
        for i in lst:
            if "check" not in i[0]:
                writer.writerow(i)