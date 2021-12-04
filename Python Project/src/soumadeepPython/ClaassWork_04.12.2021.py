# # WAP to find no of occurance of each letter in a String using dictionary.
String = input("Enter String: ")
d = {}
s = ""
for i in range(0, len(String)):
    if(String[i] not in s):
        c = String.count(String[i])
        d[String[i]] = c
        s += String[i]
print(d)


# # WAP convert the following String into dictionary.
# # "Vijay=23,Ganesh=20,Lakshmi=19,Nikhil=22"
String = "Vijay=23,Ganesh=20,Lakshmi=19,Nikhil=22"
String += ","
d = {}
p, st, st1 = 0, "", 0
for i in range(0, len(String)):
    if(String[i] == "="):
        st = String[p:i]
        p = i+1
    if(String[i] == ","):
        st1 = int(String[p:i])
        p = i+1
        d[st] = st1
print(d)


# # Write a program accept a number and check whether it is divisible by 11 or not. If not divisible by 11 then display the nearest number which is divisible by 11
number = int(input("Enter number: "))
r = number % 11
if(r == 0):
    print("Divisible by 11")
elif(r <= 11//2):
    print(f"Nearest No: {number-r}")
else:
    print(f"Nearest Number is : {number-r+11}")


# # WAP accept roll as key and values are another dictionary which contained name, age, class of 10 students. Search the student whose name is given by the user as input.
dr, dv = {}, {}
for i in range(1, 11):
    dv = {}
    roll = int(input("Enter Roll No: "))
    name = input("Enter name: ")
    age = input("Enter age: ")
    Class = input("Enter class: ")
    dv["name"], dv["age"], dv["class"] = name, age, Class
    dr[roll] = dv
name = input("Enter name to be searched: ")
for i in dr:
    if(dr[i]["name"] == name):
        print("Student Roll: ", i)
        print("Age: ", dr[i]["age"])
        print("Class: ", dr[i]["class"])
