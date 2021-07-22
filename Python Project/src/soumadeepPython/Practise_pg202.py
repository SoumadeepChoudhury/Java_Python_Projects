# Read Today's date from the user & display how many days are left in the month.


user_date = input("Enter today's date: ")
user_date = user_date.split('/')
date = int(user_date[0])
month = int(user_date[1])
year = int(user_date[2])
rem_date = 0
if(month == 2 and year % 4 == 0):
    rem_date = 29-date
elif(month == 2 and year % 4 != 0):
    rem_date = 28-date
elif(month <= 7 and month % 2 == 0):
    rem_date = 30-date
elif(month <= 7 and month % 2 != 0):
    rem_date = 31-date
elif(month > 7 and month % 2 != 0):
    rem_date = 30-date
elif(month > 7 and month % 2 == 0):
    rem_date = 31-date
print(rem_date)
