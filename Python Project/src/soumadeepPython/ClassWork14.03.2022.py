# WAP accept 15 words in a list display only palindrome word and special word.
UserList = eval(input("Enter 15 words in a list: "))
for i in UserList:
    if i == i[::-1]:
        print(f"{i} is a palindrome word")
    elif i[0] == i[-1]:
        print(f"{i} is a special word")
