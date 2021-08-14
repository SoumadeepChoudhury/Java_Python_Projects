# Write 3 lines of code that assigns first 5 multiples of a number to 5 variables and then print them.


user_input = int(input("Enter A number: "))
a, b, c, d, e = user_input*1, user_input * \
    2, user_input*3, user_input*4, user_input*5
print(a, b, c, d, e)
