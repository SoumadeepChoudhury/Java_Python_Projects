# # WAP accept float no. and a whole no. CHeck which is greater by how much..

float_number = float(input("Enter float number: "))
whole_number = int(input("Enter int number: "))
if(float_number > whole_number):
    print("Float no. is greater by: ", (float_number-whole_number))
else:
    print("Whole no. is greater by: ", (whole_number-float_number))


# # WAP accept a no. and check whether greater than 10 and even ...

number = int(input("Enter number: "))
if(number > 10 and number % 2 == 0):
    print("Number is even and greater than 10")
elif(number > 10 and number % 2 != 0):
    print("Number is not even but greater than 10")
elif(number < 10 and number % 2 == 0):
    print("Number is less than 10 but even")
else:
    print("Number is not greater than 10 and not even")


# # WAP accept salary and age of an employee. If age is between 40 to 55 then they will get 15.5% bonus in salary else they will get 7% bonus of the salary. Display total salary of an employee.

salary = float(input("Enter salary: "))
age = int(input("Enter age: "))
net_salary = 0
if(age > 40 and age < 55):
    net_salary = salary+(15.5/100*salary)
else:
    net_salary = salary+(7/100*salary)
print("Net Salary: ", net_salary)
