# WAP program accept name of a student ,roll ,sec & total marks out of 600 then display name roll sec and % marks of the student.


name = input("Enter name: ")
roll = int(input("Enter roll: "))
sec = input("Enter Sec: ")
marks = float(input("Enter total marks out of 600: "))

percent = marks/6
print("Name: ", name, "\nRoll: ", roll, "\nSec: ",
      sec, "\nPercent: ", percent, end="%")
