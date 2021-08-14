#  get distinct characters and their count in a String


string = input("Enter String: ")
c = 0
for i in range(65, 91):
    c = 0
    for j in range(0, len(string)):
        if(string[j] == chr(i)):
            c += 1
    if c > 0:
        print("", chr(i), " is ", c, " times.")
c = 0
for i in range(97, 123):
    c = 0
    for j in range(0, len(string)):
        if(string[j] == chr(i)):
            c += 1
    if c > 0:
        print("", chr(i), " is ", c, " times.")
