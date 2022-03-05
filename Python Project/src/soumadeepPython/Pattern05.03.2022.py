"""
1
# #
3 3 3
# # # #
"""

userVal = int(input("Enter number of rows : "))
for i in range(1, userVal+1):
    if(i % 2 == 0):
        print("# "*i, end=" ")
    else:
        print((str(i)+" ")*i, end=" ")
    print(" ")

"""
1
# #
2 2 2
# # # #
3 3 3 3 3
"""

userVal = int(input("Enter number of rows : "))
x = 1
for i in range(1, userVal+1):
    if(i % 2 == 0):
        print("# "*i, end=" ")
    else:
        print((str(x)+" ")*i, end=" ")
        x += 1
    print(" ")

# WAP accept name with first,middle and last. Display last name followed by first and middle.
userInp = input("Enter name: ")
userName = userInp.split(" ")
print(userName[-1], end=" ")
for i in range(0, len(userName)-1):
    print(userName[i], end=" ")


# WAP accept name with first,middle and last. Display last name followed by first and middle.
userInp = input("Enter name: ")
userName = userInp.split(" ")
print(userName[-1], end=".")
for i in range(0, len(userName)-1):
    print(userName[i][0], end=".")
