'''
ABCDE
BCDE
CDE
DE
E

The string is to be replaced by user Input string.
'''
userInp = input("Enter String: ")
for i in range(len(userInp)):
    print(" ".join(userInp[i:]))


# WAP accept a string. Convert the string to uppercase. Count and output the number of double letter sequence that exists in the string.
userInp = input("Enter sentence: ")
count = 0
for i in range(len(userInp)-1):
    if userInp[i] == userInp[i+1]:
        count += 1
print(count)


# WAP accept a string and display maximum occurence character in the string.
userInp = input("Enter String: ")
count = 0
char = ''
for i in userInp:
    if count < userInp.count(i):
        count = userInp.count(i)
        char = i
print(char)
