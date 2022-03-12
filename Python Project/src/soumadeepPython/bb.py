# WAP accept sentence tell the first letter of each word to capital and display the new sentence.
userInp = input("Enter sentence: ").split(" ")
s = ''
for i in range(len(userInp)):
    s += userInp[i][0].upper()+userInp[i][1:]+" "
print(s)


# WAP accept the setence and reverse each word of the sentence and display it.
userInp = input("Enter sentence: ").split(" ")
for i in range(len(userInp)):
    userInp[i] = userInp[i][::-1]
print(' '.join(map(str, userInp)))
