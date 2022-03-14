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
