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
rollNo=int(input("Enter Roll No to search: "))
try:
    while True:
        data=pickle.load(file)
        if data["roll"]==rollNo:
            print(data)
except EOFError:
    file.close()