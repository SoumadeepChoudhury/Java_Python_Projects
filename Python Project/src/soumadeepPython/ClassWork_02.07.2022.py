# Program in python to type text in a file till ~ is pressed as rightmost character.
file=open("file.txt","a")
while True:
    fileinput=input("Enter text: ")
    if fileinput.endswith('~'):
        file.write(fileinput[:len(fileinput)])
        break
    else:
        file.write(fileinput)