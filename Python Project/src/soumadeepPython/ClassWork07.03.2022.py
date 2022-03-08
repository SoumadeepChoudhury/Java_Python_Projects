import time
# Twisted PigLatin........
userInp = input("Enter word: ")
print(userInp[1:]+userInp[0]+"ay")


# Write a loop that prints out the index of every 'i' in 'Mississippi'
word = "Mississippi"
for i in range(len(word)):
    if word[i] == 'i':
        print(i, end=' ')


# WAP to check whether one word is prefix of other...
userInp1 = input("Enter 1st word: ")
userInp2 = input("Enter 2nd word: ")
if userInp2.startswith(userInp1) or userInp1.startswith(userInp2):
    print("Yes one is prefix with other...")
else:
    print("Not prefix of other")


# WAP to follow the following format.... if the user input "Mississippi" and 's' it should print 'MiSSiSSippi'

Userword = input("Enter word: ")
Userletter = input("Enter letter: ")
print(Userword.replace(Userletter, Userletter.upper()))


# WAP to make the function of ATM
USERNAME = "ABCD"
PASSWORD = "noone"
i = 0
while True:
    i += 1
    username = input("Enter Username: ")
    userpass = input("Enter password: ")
    if username == USERNAME and userpass == PASSWORD:
        print("MATCHED")
        break
    else:
        print("Not Matched..")
    if i % 3 == 0:
        time.sleep(3)
