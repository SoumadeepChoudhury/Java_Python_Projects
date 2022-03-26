# WAP that reads two times in military format(Eg: 0900,1730) and prints the number of hours and minutes between two times.
time1 = input("Please enter the first time: ")
time2 = input("Please enter the second time: ")
time1_Mins = int(time1[:2]) * 60 + int(time1[2:])
time2_Mins = int(time2[:2]) * 60 + int(time2[2:])
diff = time2_Mins - time1_Mins
hrs = diff // 60
mins = diff % 60

print(f'{hrs} hours {mins} minutes')
