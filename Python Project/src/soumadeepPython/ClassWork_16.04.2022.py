# Swaping values of two variables using recursion.
temp = 0


def recr(x, y, i=0):
    if i == 0:
        xy = x*y
        recr(xy, y, 1)
    else:
        y = x//y
        x = x//y
        print('Value of x: ', x)
        print('Value of y: ', y)


userInp1 = int(input("Enter 1st number x: "))
userInp2 = int(input("Enter 2nd number y: "))
recr(userInp1, userInp2)
