# WAP accept 15 words in a list display only palindrome word and special word.
UserList = eval(input("Enter 15 words in a list: "))
palindrome = []
special = []
for i in UserList:
    if i == i[::-1]:
        palindrome.append(i)
    elif i[0] == i[-1]:
        special.append(i)
print(i for i in palindrome)
print(i for i in special)

# WAP accept a string in uppercase.Convert all letters of the word other than the first letter to lowercase. Display the new string...
userInp = input("Enter a String in uppercase: ").upper().split(" ")
for i in userInp:
    print(i[0]+i[1:].lower(), end=" ")


# WAP input a string. Print the new string after converting every alternate letter to uppercase and next immidiate letter in lower case. Special character remains same
UserInp = input("Enter string: ").strip()
ft = UserInp[0].isupper()
print(UserInp[0], end="")
if ft:
    for i in UserInp[1:]:
        if i == " ":
            print(i, end=" ")
        if UserInp.index(i) % 2 == 0:
            print(i.upper(), end="")
        if UserInp.index(i) % 2 != 0:
            print(i.lower(), end="")
else:
    for i in UserInp[1:]:
        if i == " ":
            print(i, end="")
        if UserInp.index(i) % 2 == 0:
            print(i.lower(), end="")
        if UserInp.index(i) % 2 != 0:
            print(i.upper(), end="")

# WAP to count and print the word that has at least one consecutive pair of alphabets. Eg: MODEM IS AN ELECTRONIC DEVICE should output as MODEM and DEVICE and print 2
userInp = input("Enter sentence: ").strip().upper().split(" ")
count = 0
for i in range(len(userInp)):
    for j in range(len(userInp[i])-1):
        if chr(ord(userInp[i][j])+1) == userInp[i][j+1]:
            count += 1
            print(userInp[i], end=" ")
            break
print(f"\nNo of words are {count}")
