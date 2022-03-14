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
