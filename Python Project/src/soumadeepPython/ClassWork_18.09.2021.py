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
