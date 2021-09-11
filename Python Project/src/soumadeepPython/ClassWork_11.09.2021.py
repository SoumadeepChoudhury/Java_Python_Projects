# # WAP to create a function in python that calculate area of the circle and return the value. Access the radius and call the above function.

def Area(r):
    return (3.14*r*r)


radius = int(input("Enter radius: "))
area = Area(radius)
print(f"The area of circle is : {area}")
