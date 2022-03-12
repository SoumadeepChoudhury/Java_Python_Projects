# WAP accept sentence tell the first letter of each word to capital and display the new sentence.
userInp = input("Enter snetence: ").split(" ")
s = ''
for i in range(len(userInp)):
    s += userInp[i][0].upper()+userInp[i][1:]+" "
print(s)
