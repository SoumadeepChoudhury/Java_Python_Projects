# Accept three sides of a triangle & display perimeter and Area.

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))
perimeter = side3+side1+side2
s = perimeter/2
area = (s*(s-side1)*(s-side2)*(s-side3))**(0.5)
print("Perimeter: ", perimeter, "\nArea: ", area)
