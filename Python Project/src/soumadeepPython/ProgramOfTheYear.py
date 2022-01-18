'''You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name
2: Then sort based on age
3: Then sort by height.
The priority is that name > age > height.
If the following tuples are given as input to the program:
Tom, 19, 80
John, 20, 90
Jony, 17, 91
Jony, 17, 93
Json, 21, 85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'),
 ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]'''

# Input
input_list = []
while True:
    choice = int(input("Enter 1 to entry in fields or 0 to exit. "))
    if choice == 1:
        tup = tuple()
        for i in input("Enter Name, Age, Height: ").split(","):
            tup += (i,)
        input_list.append(tup)
    else:
        break
# Name Sort
for k in range(len(input_list)-1):
    for i in range(len(input_list)-1):
        if(input_list[i][0] > input_list[i+1][0]):
            x = input_list[i]
            input_list[i] = input_list[i+1]
            input_list[i+1] = x

# Age Sort
for k in range(len(input_list)-1):
    for i in range(len(input_list)-1):
        if(input_list[i][0] == input_list[i+1][0] and input_list[i][1] > input_list[i+1][1]):
            x = input_list[i]
            input_list[i] = input_list[i+1]
            input_list[i+1] = x

# Height Sort
for k in range(len(input_list)-1):
    for i in range(len(input_list)-1):
        if(input_list[i][0] == input_list[i+1][0] and input_list[i][1] == input_list[i+1][1] and input_list[i][2] > input_list[i+1][2]):
            x = input_list[i]
            input_list[i] = input_list[i+1]
            input_list[i+1] = x

print(input_list)
