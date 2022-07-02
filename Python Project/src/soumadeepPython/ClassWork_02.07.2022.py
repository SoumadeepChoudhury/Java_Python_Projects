# Program in python to type text in a file till ~ is pressed as rightmost character.
file=open("file.txt","a")
while True:
    fileinput=input("Enter text: ")
    if fileinput.endswith('~'):
        file.write(fileinput)
        break
    else:
        file.write(fileinput)
file.close()

# WAP to read first 5 lines from the text file.
file=open("file.txt")
for i in range(5):
    print(file.readline())