############## HOMEWORK ################

# # WAP to enter names of the employees and their salaries as input and store them in a dictionary.
employees = {}
for _ in range(int(input("Enter number of Employees: "))):
    names, salary = eval(input("Enter Name, Salary: "))
    employees[names] = salary
print(employees)


# # WAP To convert a number entered by the user into its corresponding number in words. For example, if the input is 876 then the output should be 'Eight Seven Six'.
Num_Words = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
             5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
l = []
user_Inp = int(input("Enter whole Number: "))
while(user_Inp > 0):
    d = user_Inp % 10
    l.append(Num_Words[d])
    user_Inp //= 10
l = l[::-1]
print(' '.join([i for i in l]))
