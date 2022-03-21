'''
ABCDE
BCDE
CDE
DE
E
'''
userInp = int(input("Enter no of rows: "))
for i in range(65, 65+userInp):
    for j in range(i, 65+userInp):
        print(chr(j), end=' ')
    print()
