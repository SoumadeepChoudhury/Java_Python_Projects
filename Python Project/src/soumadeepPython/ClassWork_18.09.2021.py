# # Write a program that implements a user defined function that accepts Principal Amount, Rate, Time, Number of Times the interest is compounded to calculate and displays compound interest. (Hint: CI=((P*(1+R/N))NT)

def CI(P, R, T, N):
    ci = (P*((1+R/N)**(N*T)))
    print(f"The value of Compound Interest is {ci}")


P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))
N = float(input("Enter Number of Times the interest is componded: "))
CI(P, R, T, N)
