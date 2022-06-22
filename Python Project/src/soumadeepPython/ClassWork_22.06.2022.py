# Write a program to accept string/sentences from the user till the user enters “END” to. Save the data in a text file and then display only those sentences which begin with an uppercase alphabet.
userInput=""
while userInput!="END":
    userInput=input("Enter string/sentence: ")
    with open("tt.txt","a") as file:
        if userInput!="END":
            file.write(userInput+'\n')
with open("tt.txt",'r') as file:
    for line in file:
        if line[0].isupper():
            print(line)