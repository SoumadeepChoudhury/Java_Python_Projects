# Accept name, roll no., sec & marks scored out of 40. Display name,roll,sec,& % of marks obtained

name = input("Enter name: ")
roll = int(input("Enter roll no. : "))
sec = input("Enter section : ")
marks = float(input("Enter marks out of 40: "))
percent = (marks/40)*100
if percent <= 100.0:
    print("Name: ", name, "\nRoll No.: ", roll,
          "\nSec.: ", sec, "\nPercentage: ", percent, end="%")
    print()
else:
    print("Enter marks properly")
