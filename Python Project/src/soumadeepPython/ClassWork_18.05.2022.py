## WAP to read a csv or text file and display number of words and the words starts with "A"
import csv
file=input("Enter the file name with extension: ")
fileHandle=open(file,"r")
count=0
if ".csv" in file:
    context=csv.reader(fileHandle)
    for rows in context:
        for words in rows:
            if words.startswith("A"):
                count+=1
                print(words)
elif ".txt" in file:
    for words in fileHandle:
        if words.startswith("A"):
            count+=1
            print(words)
print(count,"no of words")

## WAP to display details the roll no from a dat file
import pickle
file=open(input("Enter name of .dat file with extension : "),"rb")
while True:
    name=input("Enter Name: ")
    Class=input("Enter Class")
    ROll=input("Enter Roll: ")
    pickle.dump({"Name":name,"Class":Class,"Roll":ROll})
    if input("Wanna enter more? Y/N")=='N':
        break
rollNo=int(input("Enter Roll No to search: "))
try:
    while True:
        data=pickle.load(file)
        if data["Roll"]==rollNo:
            print(data)
except EOFError:
    file.close()