# Write a program to accept string/sentences from the user till the user enters “END” to. Save the data in a text file and then display only those sentences which begin with an uppercase alphabet.
userInput=""
while userInput!="END":
    userInput=input("Enter string/sentence: ")
    with open("file.txt","a") as file:
        file.write(userInput)
with open("file.txt",'r') as file:
    for line in file:
        if line[0].isupper():
            print(line)