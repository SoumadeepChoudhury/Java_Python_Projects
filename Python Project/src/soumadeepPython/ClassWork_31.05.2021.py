# # WAP accept a number and check even or odd..

number = int(input("Enter number: "))
if(number == 0):
    print("Zero")
elif(number % 2 == 0):
    print("Even")
else:
    print("Odd")


# # WAP accept three subject marks . Calculate % marks. and display grade as per following condition...
# # 80 - 100 > A... ..... 60 -<80 >> B..... 40- 60 >> C else D

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
percent = (marks1+marks2+marks3)/3
if(percent >= 80 and percent <= 100):
    print("Grade A")
elif(percent >= 60 and percent < 80):
    print("Grade B")
elif(percent >= 40 and percent < 60):
    print("Grade C")
else:
    print("Grade D")
