# Ms. Snehal wants to design the report card of half yearly exams for her class. Before designing the report card, she first needs to input the name of each student and his/her class, DOB, Father's name, Mother's Name, and marks in five subjects (each out of 100). She also needs calculate the total marks and percentage, and assign the grade as per the given criteria:
'''
<40 ----> D
40-50---->C
51-60----->C+
61-70------>B
71-80----->B+
81-90----->A
>90 ------> A+
'''
name=input("Name of student: ")
class_=input("Class: ")
father_name=input("Father's Name: ")
mother_name=input("Mother's Name: ")
dob=input("Date Of Birth in DD/MM/YYYY: ")
eng=int(input("English: "))
hindi=int(input("Hindi: "))
science=int(input("Science: "))
sst=int(input("Social Studies: "))
math=int(input("Mathematics: "))
total_marks=eng+hindi+science+sst+math
percentage=total_marks/5
grade=''
if percentage<=40:
    grade='D'
elif percentage>40 and percentage<=50:
    grade='C'
elif percentage>50 and percentage<=60:
    grade='C+'
elif percentage>60 and percentage<70:
    grade='B'
elif percentage>71 and percentage<80:
    grade='B+'
elif percentage>80 and percentage<90:
    grade='A'
elif percentage>90:
    grade='A+'

print(f"_____________REPORT CARD______________\nName: {name}\t\t\t\tClass: {class_}\nFather's Name: {father_name}\t\tMother's Name: {mother_name}\nDate of Birth: {dob}\nEnglish: {eng}\nHindi: {hindi}\nScience: {science}\nSocial Studies: {sst}\nMathematics: {math}\nTotal Marks: {total_marks}\nPercentage: {percentage}\nOverall Grade: {grade}")