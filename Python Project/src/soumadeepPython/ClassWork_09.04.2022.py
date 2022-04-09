# Design a program to accept a day number( between 1 and 366),year(in 4 digits ) from the user to generate and display the corresponding date. Also accept 'N'(1<=N<=100) from the user to compute and display the future date corresponding to 'N' days after the generated date. Display error message if the value of the day number,year and N are not with in the limit or not according to the condition specified.
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthNames = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE",
              "JULY", "AUGUST", "SEPTEMBER",   "OCTOBER", "NOVEMBER", "DECEMBER"]


def leapYear(userYear: int) -> bool:
    global monthDays
    if (userYear % 400 == 0 or userYear % 4 == 0):
        monthDays[1] = 29
        return True
    else:
        return False


def dateComp(userdayNum: int, userYear: int):
    _ = leapYear(userYear)
    global monthNames, monthDays
    date = 0
    daySum = 0
    for i in range(len(monthDays)):
        daySum += monthDays[i]
        if (daySum >= userdayNum):
            date = userdayNum + monthDays[i] - daySum
            break

    print(f'{date}th {monthNames[i]}, {userYear}')


userdayNum = int(input("Enter Day Number: "))
userYear = int(input("Enter Year: "))
N = int(input("Enter value of N: "))
afterdayNum = userdayNum+N
afteryear = userYear


if userdayNum < 1 or userdayNum > 366:
    print("Day num out of range")
elif N < 1 or N > 100:
    print("Value of N is out of range")
else:
    print("The required date: ", end='')
    dateComp(userdayNum, userYear)
    if leapYear(userYear) and afterdayNum > 366:
        afteryear += 1
        afterdayNum -= 366
    elif (afterdayNum > 365):
        afteryear += 1
        afterdayNum - +365
    print("The required later-date: ", end='')
    dateComp(afterdayNum, afteryear)


# A smith number is a composite number, the sum of whose digits is the sum of the digits of it's prime factors obtained as a result of prime factorisation. eg: 666
userNum = int(input("Enter num: "))
sumOfPrime = 0
sumOfDigit = 0
tempNum = userNum
i = 1
runs = 0
while tempNum > 0:
    sumOfDigit += tempNum % 10
    tempNum //= 10
while userNum > 0:
    count_ = 1
    if userNum % i == 0:
        for j in range(1, i):
            if i % j == 0:
                count_ += 1
        if count_ == 2:
            tempNum = i
            while tempNum > 0:
                sumOfPrime += tempNum % 10
                tempNum //= 10
            userNum //= i
            i = 2
            if sumOfDigit == sumOfPrime:
                print("Smith Number")
                runs = 1
                break
        else:
            i += 1
    else:
        i += 1

if runs == 0:
    print("Not Smith Number")
