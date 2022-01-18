'''Terrace Number is a pair of Number where on taking it's ratio there will be position where both the resulting numbers will have same digits(may be jumbled or same) and it's simplest ratio will be consecutive natural number. For eg: (1944,2592),(87480,116640),(6804,9072),(1296,972)'''

import math
userNum1, userNum2 = int(input("Enter number 1: ")), int(
    input("Enter number 2: "))
temp1, temp2 = userNum1, userNum2
gcd = math.gcd(temp1, temp2)
li = [2, 3, 5, 7, 11, 13, 17, 19]
i = 0
while True:
    if(userNum1 % li[i] == 0 and userNum2 % li[i] == 0):
        userNum1, userNum2 = userNum1//li[i], userNum2//li[i]
        i = 0
        lis1 = list(str(userNum1))
        lis2 = list(str(userNum2))
        z, k = 0, 0
        if len(lis1) == len(lis2):
            for z in lis1:
                if(z in lis2):
                    k += 1
            for z in lis2:
                if(z in lis2):
                    k += 1
            if(k == len(lis1)*2):
                print("Terrace Number" if(temp1//gcd == temp2//gcd -
                      1 or temp1//gcd == temp2//gcd+1) else "Not Terrace Number")
                break
    elif(userNum1 < 1 or userNum2 < 1 or i == len(li)-1):
        print("Not Terrace number")
        break
    else:
        i += 1
