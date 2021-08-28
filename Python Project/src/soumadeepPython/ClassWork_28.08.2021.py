# # WAP accept 10 elements in a list and display Even elements from that list.
# list_input = []
# for _ in range(10):
#     list_input.append(int(input("Enter value: ")))
# print("These are Even: ")
# for i in list_input:
#     if(i % 2 == 0):
#         print(i)


# # WAP accept 10 elements in list and accept a number and check how many times the number occurs in  the list...
list_input = []
for _ in range(10):
    list_input.append(int(input("Enter value: ")))
check_pt = int(input("Enter a number to check the occurance: "))
print(f"{check_pt} occurs {list_input.count(check_pt)} times.")

# HOMEWORK
# # WAP create a list with 15 different type elements and check whether they are digit or alphabet and count the total number of digits and alphabets and display it.
