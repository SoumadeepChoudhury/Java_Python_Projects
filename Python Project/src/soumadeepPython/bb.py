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


# WAP accept a sentence display the word that has max vowel.
userInp = input("Enter sentence: ").split(" ")
maxVowel = 0
for i in userInp:
    temp = 0
    for s in i:
        if s in 'aeiouAEIOU':
            temp += 1
        if temp > maxVowel:
            maxVowel = temp
            word = i
print(word)


'''
ABCDE
BCDE
CDE
DE
E
'''
str = "ABCDE"
for i in range(len(str)):
    for j in range(i, len(str)):
        print(str[j], end=' ')
    print()
