import math  # Globally defined for whole programs set.
import random
# # Write a program that implements a user defined function that accepts Principal Amount, Rate, Time, Number of Times the interest is compounded to calculate and displays compound interest. (Hint: CI=((P*(1+R/N))NT)


def CI(P, R, T, N):
    ci = (P*(1+R/N)**(N*T))
    print(f"The value of Compound Interest is {ci}")


P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
N = float(input("Enter Number of Times the interest is componded: "))
CI(P, R, T, N)


# # Write a program that has a user defined function to accept 2 numbers as parameters, if number 1 is less than number 2 then numbers are swapped and returned, i.e., number 2 is returned in place of number1 and number 1 is reformed in place of number 2, otherwise the same order is returned.
def swaper(num1, num2):
    if(num1 < num2):
        num1, num2 = num2, num1
        return num1, num2
    else:
        return num1, num2


num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number : "))
print(swaper(num1, num2))


# # Write a program that contains user defined functions to calculate area, perimeter or surface area whichever is applicable for various shapes like square, rectangle, triangle, circle and cylinder. The user defined functions should accept the values for calculation as parameters and the calculated value should be returned. Import the module and use the appropriate functions.
def square(side):
    # Math Module is defined at top of this page.
    area = math.pow(side, 2)
    perimeter = math.prod(4, side)
    return area, perimeter


def rectangle(length, breadth):
    area = math.prod(length, breadth)
    perimeter = math.prod(2, (sum(length+breadth)))
    return area, perimeter


def triangle(a, b, c):
    sp = sum(a, b, c)/2
    area = math.sqrt(math.prod(sp, (sp-a), (sp-b), (sp-c)))
    perimeter = sum(a, b, c)
    return area, perimeter


def circle(radius):
    area = math.prod(3.14, math.pow(radius, 2))
    perimeter = math.prod(2, 3.14, radius)
    perimeter = math.prod(2, 3.14, radius)
    return area, perimeter


def cylinder(radius, height):
    area = sum(math.prod(2, 3.14, radius, height),
               math.prod(2, 3.14, math.pow(radius, 2)))
    perimeter = sum(math.prod(4, 3.14, radius), math.prod(2, height))
    return area, perimeter


side_square = float(input("Enter side of square: "))
print(f"Data from square: {square(side_square)}")

length_rectangle = float(input("Enter length of rectangle: "))
breadth_rectangle = float(input("Enter breadth of rectangle: "))
print(
    f"The Data for rectangle: {rectangle(length_rectangle,breadth_rectangle)}")


side1_Triangle = float(input("Enter side1 of triangle: "))
side2_Triangle = float(input("Enter side2 of triangle: "))
side3_Triangle = float(input("Enter side3 of triangle: "))
print(
    f"The Data from Triangle :{triangle(side1_Triangle,side2_Triangle,side3_Triangle)}")


radius_circle = float(input("Enter radius of circle: "))
print(f"The Data from circle :{circle(radius_circle)}")


radius_cylinder = float(input("Enter radius  of Cylinder: "))
height_cylinder = float(input("Enter height of Cylinder: "))
print(f"The Data from Cylinder :{cylinder(radius_cylinder,height_cylinder)}")


# ############ HOMEWORK  #################### #
'''
Write a program that creates a GK quiz consisting of any five questions of your choice. The questions should be displayed randomly. Create a user defined function score() to calculate the score of the quiz and another user defined function remark(scorevalue) that accepts the final score to display remarks as
follows:
Marks Remarks
5 Outstanding
4 Excellent
3 Good
2 Read more to score more
1 Needs to take interest
0 General knowledge will always help you. Take it seriously.
'''
questions = ("Who is the Father of our Nation?",
             "Who was the first President of India?", "Who is known as Father of Indian Constitution?", "Which is the most sensitive organ in our body?", "Giddha is the folk dance of?")
answers = ("Mahatma Gandhi", "Rajendra Prasad",
           "B. R. Ambedkar", "Skin", "Punjab")
remarks = ("General knowledge will always help you. Take it seriously.",
           "Needs to take interest", "Read more to score more", "Good", "Excellent", "Outstanding")
scores, question_Done_Number = 0, []


def score():
    print("QUIZ BEGINS.......")
    global questions, answers, scores
    while True:
        if(len(question_Done_Number) == 5):
            break
        # Random Module imported at top.
        question_Number = random.randint(0, 4)
        if(question_Number not in question_Done_Number):
            print(questions[question_Number])
            user_Answer = input("ANSWER: ")
            if(user_Answer == answers[question_Number]):
                scores += 1
            question_Done_Number.append(question_Number)
        else:
            continue
    return scores


def remark(scores):
    global remarks
    print(f"Your REAMRKS: {remarks[scores]}")


start = input("Press Enter to Start the QUIZ......")
if len(start) == 0:
    scores = score()
    remark(scores)
else:
    print("Need to Press ENTER.... SORRY! Better Luck Next Time...")
