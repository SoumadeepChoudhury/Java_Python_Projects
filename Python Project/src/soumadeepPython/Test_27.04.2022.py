# String Fibonacci series.....1,1,2,3,5...
from turtle import title


def FiboString(n, x="a", y="b", z="ba"):
    term = z+y
    print(x, y, z, end=', ')
    a, b, c = 1, 1, 2
    for _ in range(4, n+1):
        a = b
        b = c
        c = a+b
        for j in range(c):
            if j >= len(term):
                print(term[j-len(term)], end=", ")
            else:
                print(term[j], end=", ")


def accept():
    return int(input("Enter n: "))


FiboString(accept())


# Q2) Q4 from book..
def movie(title, year, rating):
    print(title, year)
    if rating > 1 and rating < 2:
        print("Flop")
    if rating >= 2.1 and rating <= 4.0:
        print("Semi Hit")

    if rating >= 4.1 and rating <= 6.0:
        print("Hit")

    if rating >= 6.1 and rating <= 8.0:
        print("Super Hit")


def accept():
    title = input("Enter Title: ")
    year = input("Enter Year of Release: ")
    rating = input("Enter Rating from 1.0 to 8.0: ")
    return title, year, rating


title, year, rating = accept()
movie(title, year, rating)
