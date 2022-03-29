# WAP that reads two times in military format(Eg: 0900,1730) and prints the number of hours and minutes between two times.
time1 = input("Please enter the first time: ")
time2 = input("Please enter the second time: ")
time1_Mins = int(time1[:2]) * 60 + int(time1[2:])
time2_Mins = int(time2[:2]) * 60 + int(time2[2:])
diff = time2_Mins - time1_Mins
hrs = diff // 60
mins = diff % 60
print(f'{hrs} hours {mins} minutes')


# WAP to print a table with two columns that helps convert pounds to kilograms
userInp = int(input("Enter amount in pounds: "))
print(f"Pounds | Kilograms \n{userInp}\t| {userInp*0.453592}")

# WAP to print a table with two columns that helps convert miles to kilometers.
userInp = int(input("Enter distance in miles: "))
print(f"Miles | Kilometers \n{userInp}\t| {userInp*1.60934}")


# WAP that reads a date as an integer in the format MMDDYYYY.The program will call a function that prints out the date in the format <Month Name> <day>,<year>.
userInp = input("Enter date in MMDDYYYY format: ")
MONTH_NAME = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']


def printDate():
    month, day, year = int(userInp[:2]), int(userInp[2:4]), int(userInp[4:])
    if (month > 12 or month < 1 or day > 31 or day < 1 or (day > 28 and month == 2) or len(userInp) != 8):
        print("Invalid Input")
    else:
        print(f"{MONTH_NAME[month-1]} {day},{year}")


printDate()

# WAP that reads a date as an integer N from keyword computes and displays the sum of the numbers from N to (2*N) if N is nonnegative. If N is a negative number,then it's sum of the number from (2*N) to N.The starting and ending points are included in the sum.
userInp = int(input("Enter value of N: "))
sum = 0
if userInp > 0:
    for i in range(userInp, (2*userInp)+1):
        sum += i
else:
    for i in range((2*userInp), userInp+1):
        sum += i
print(sum)

# One foot eqauls 12 inches.Write a function that accepts a length written in feet as an argument and returns this length written in inches.Write a second function that asks user for a number of feet and returns this value.Write a third function that accepts a number of inches and display this to the screen. Use these three functions to write a program that asks the user for a number of feet and tells them the corresponding numer of inches.


def feetInch(feet):
    return feet*12


def askUser():
    return int(input("Enter value in feet: "))


def displayInch(inch):
    print(f"Inches: {inch}")


displayInch(feetInch(askUser()))


# WAP that asks the user the day number in a year in the range 2 to 365 and asks the first day of the year - Sunday or Monday or Tuesday etc. Then the program should display the day on the day-number that has been input.
userInp = int(input("Enter any day number from 2 to 365: "))
startDay = input("Enter first day of the year: ")
DAYS = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']
if userInp < 2 or userInp > 365:
    print("Invalid Input")
else:
    startDayIdx = DAYS.index(str.upper(startDay[0])+startDay[1:].lower())
    currDayIdx = userInp % 7 + startDayIdx - 1

    if currDayIdx >= 7:
        currDayIdx = currDayIdx - 7

    print(f"Day on day number {userInp} : {DAYS[currDayIdx]}")


# WAP the accepts two integer from the user and prints a massage saying if first number is divisible by the second number of if it is not.
userInp1, userInp2 = int(input("Enter first number: ")), int(
    input("Enter second number: "))
if userInp1 % userInp2 == 0:
    print("Divisible by 2nd number.....")
else:
    print("Not Divisible by 2nd number.....")


# WAP that calculates and prints the number of seconds in a year.
print(f"Seconds in a year: {365*24*60*60}")

# WAP that returns True if the input number is an even number,False otherwise.


def EvenOdd():
    if int(input("Enter number: ")) % 2 == 0:
        return "Even"
    else:
        return "Odd"


# WAP to print one of the words negative,zero, or positive, according to whether variable x is less  than zero,zero,or greater than zero,respectively.
x = int(input("Enter value of x: "))
if x > 0:
    print("Positive")
elif(x == 0):
    print("Zero")
else:
    print("Negative")
