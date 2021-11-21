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


# # Write a program that repeatedly asks the user to enter product names and prices. Store all of these in a dictionary keys are the product names and whose values are the prices. When the user is done entering products and prices, allow them to repeatedly enter a product name and print the corresponding  price or a message if the product is not in the dictionary.
productItems = {}
while True:
    name, price = input("Enter name: "), float(
        input("Enter price of the product: "))
    productItems[name] = price
    if(input("Do you want to enter more products name ? Y/N").lower() == 'n'):
        break
while True:
    nameCheck = input("Enter product name: ")
    print(f"The Price of  {nameCheck} is : {productItems[nameCheck]}" if nameCheck in productItems.keys(
    ) else "Not in the list of items. Try another items.")
    if(input("Do you check more products name ? Y/N").lower() == 'n'):
        break


'''Create a dictionary with keys are month names and whose values are the number of days in the corresponding month.
a) Ask the user to enter a month name and use a dictionary to tell how many days are in a month.
b) Print out all the keys in the alphabetical order.
c) Print out all of the months with 31 days.
d) Print out the (key-value) pairs sorted by the number of days in each month.
'''
monthDays = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
             'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
month = input("Enter month name: ")
print(
    f"The number of months in {month} is {monthDays[month] if month in monthDays else 'Not Found'}")
print(sorted(monthDays, reverse=False))

for i in monthDays:
    if(i[1] == 31):
        print(i)
sort = sorted([(i, j) for j, i in monthDays.items()])
print([(i, j) for i, j in sort])


# # Given the dictionary x = {'k1':'v1','k2':'v2','k3':'v3'}, create a dictionary with the opposite mapping that is written writer program to create the dictionary as: inverted_x = {'v1':'k1','v2':'k2','v3':'k3'}
x = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
keys = list(x.keys())
values = list(x.values())
inverted_x = {}
for i in range(len(keys)):
    inverted_x[values[i]] = keys[i]
print(inverted_x)


# # Given 2 dictionaries saying D1 and D2. Write a program that lists the overlapping keys of the two dictionaries, that is, if a key of D1 is also a key of D2, then list it.
D1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
D2 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
D1Keys = list(D1.keys())
D2Keys = list(D2.keys())
x = D2Keys if len(D2Keys) < len(D1Keys) else D1Keys
y = D1Keys if(x == D2Keys) else D2Keys
for i in (x):
    if(i in y):
        print(i)


# # Write a program that checks if two same values in a dictionary have different keys. That is, for dictionary D1 = { ‘a’ : 10, ‘b': 20, ‘c’ : 10}, the program should print “2 keys have same values” and for dictionary D2 = { ‘a’ : 10, ‘b’ : 20, ‘c’ : 30} , the program should print “No keys have same values”.
D1 = {'a': 10, 'b': 20, 'c': 10}
values = list(D1.values())
x = "000"
for i in values:
    if x != i and values.count(i) > 1:
        print(f"{values.count(i)} keys have same values")
    x = i


# # WAP to check if a dictionary is contained in another dictionary.
# # d1 = {1:11,2:12}
# # d2 = {1:11,2:12,3:13,4:15} ........... Therefore d1 is contained in d2.
d1 = {1: 11, 2: 12}
d2 = {1: 11, 2: 12, 3: 13, 4: 15}
d1Pairs = list(d1.items())
d2Pairs = list(d2.items())
for i in d1Pairs:
    if i in d2Pairs:
        print("First Dictionary is contained in another Dictionary")
        break


# # A dictionary has values in the form of list of numbers. Write a program to create a new dictionary D2 having same keys as D1 but values as the sum of the list elements.
D1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
values = list(D1.values())
D2 = {}
keys = list(D1.keys())
for i in range(len(keys)):
    D2[keys[i]] = sum(values[i])
print(D2)
