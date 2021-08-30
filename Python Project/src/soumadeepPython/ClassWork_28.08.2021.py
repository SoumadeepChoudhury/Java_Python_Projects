# # WAP accept 10 elements in a list and display Even elements from that list.
list_input = []
for _ in range(10):  # input in list
    list_input.append(int(input("Enter value: ")))
print("These are Even: ")
for i in list_input:  # Checking in list
    if(i % 2 == 0):
        print(i)


# # WAP accept 10 elements in list and accept a number and check how many times the number occurs in  the list...
list_input = []
for _ in range(10):  # Input in list
    list_input.append(int(input("Enter value: ")))
check_pt = int(input("Enter a number to check the occurance: "))
# Checking and printing the result.
print(f"{check_pt} occurs {list_input.count(check_pt)} times.")

# HOMEWORK
# # WAP create a list with 15 different type elements and check whether they are digit or alphabet and count the total number of digits and alphabets and display it.
user_Input_List = []
alphaCount, digiCount, alphaDigi_Count = 0, 0, 0
print("Enter different types of entries for checking: ")
for _ in range(15):  # For user Input.
    user_input = input("Enter data: ")
    user_Input_List.append(user_input)
for entries in user_Input_List:
    if(entries.isalpha()):
        alphaCount += 1
        print(f"{entries} is Alpha")
    elif(entries.isdigit()):
        digiCount += 1
        print(f"{entries} is/are Digit/s")
    elif(entries == ""):
        print("No Input")
    else:
        alphaDigi_Count += 1
        print(f"{entries} containes alpha as well as digits.")
