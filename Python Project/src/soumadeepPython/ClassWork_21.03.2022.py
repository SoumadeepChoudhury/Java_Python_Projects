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


# WAP accept a sentence in uppercase and change the each vowel with next vowel.
userInp = input("Enter sentence: ").upper()
vowel = ['A', 'E', 'I', 'O', 'U']
# for i in range(len(userInp)):
#     if userInp[i] in vowel:
#         userInp = userInp.replace(userInp[i], vowel[vowel.index(
#             userInp[i])+1 if userInp[i] != 'U' else 0])
userInp = userInp.replace('A', 'E')
userInp = userInp.replace('E', 'I')
userInp = userInp.replace('I', 'O')
userInp = userInp.replace('O', 'U')
userInp = userInp.replace('U', 'A')
print(userInp)

# WAP accept ten names and print those names which starts with given letter by user.
userInpList = eval(input("Enter 10 names: "))
char = input("Enter character: ")
for i in userInpList:
    if i[0] == char:
        print(i)
