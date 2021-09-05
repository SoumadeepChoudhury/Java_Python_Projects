'''
# # WAP menu driven to :
• Append an element
• Insert an element
• Append a list to the given list
• Modify an existing element
• Delete an existing element from its position
• Delete an existing element with a given value
• Sort the list in ascending order
• Sort the list in descending order
• Display the list.
'''

list1 = [1, 8, 4, 7, 45, 45]
print("Enter choice from here: ")
print(" 1. Append an element")
print(" 2. Insert an element at the desired position")
print(" 3. Append a list to the given list")
print(" 4. Modify an existing element")
print(" 5. Delete an existing element by its position")
print(" 6. Delete an existing element by its value")
print(" 7. Sort the list in ascending order")
print(" 8. Sort the list in descending order")
print(" 9. Display the list")
user_choice = int(input("Enter Choice: "))
# Append an element
if user_choice == 1:
    user_element = int(input("Enter the element to be appended: "))
    list1.append(user_element)
    print("The element has been appended")
# Insert an element at the desired position
elif user_choice == 2:
    user_element = int(input("Enter the element to be inserted: "))
    position = int(input("Enter the position:"))
    list1.insert(position, user_element)
    print("The element has been inserted")
# Append a list to the given list
elif user_choice == 3:
    newList1 = int(input("Enter the list to be appended: "))
    list1.extend(newList1)
    print("The list has been appended")
# Modify an existing element
elif user_choice == 4:
    i = int(input("Enter the position of the element to be modified: "))
    if i < len(list1):
        newUserElement = int(input("Enter the new element: "))
        oldUserElement = list1[i]
        list1[i] = newUserElement
        print("The element", oldUserElement, "has been modified")
    else:
        print("Position of the element is more than the length of list")
# Delete an existing element by position
elif user_choice == 5:
    i = int(input("Enter the position of the element to be deleted: "))
    if i < len(list1):
        user_element = list1.pop(i)
        print("The element", user_element, "has been deleted")
    else:
        print("Position of the element is more than the length of list")
# Delete an existing element by value
elif user_choice == 6:
    user_element = int(input("Enter the element to be deleted: "))
    if user_element in list1:
        list1.remove(user_element)
        print("The element", user_element, "has been deleted")
    else:
        print("Element", user_element, "is not present in the list")
# List in sorted order
elif user_choice == 7:
    list1.sort()
    print("The list has been sorted")
# List in reverse sorted order
elif user_choice == 8:
    list1.sort(reverse=True)
    print("The list has been sorted in reverse order")
# Display the list
elif user_choice == 9:
    print("The list is:", list1)
else:
    print("In valid choice")


# # WAP accept ten integer elements in a list and sort the list ascending and descending in new list. Display the difference between two list of each element.
input_list = []
for _ in range(10):
    user_element = int(input("Enter integer element: "))
    input_list.append(user_element)
ascending = sorted(input_list)
descending = sorted(input_list, reverse=True)
print("Ascending: ", ascending)
print("Descending: ", descending)

for i in range(len(input_list)):
    print(
        f"Diff between element {i} of booth the list is: {descending[i]-ascending[i]}")


############### HOMEWORK ################

# # WAP to increment the elements of a list with a number.
user_List = eval(input("Enter a list conatining integer elemets: "))
number = int(input("Enter number by which increament is to be done: "))
for i in range(len(user_List)):
    user_List[i] += number
print(f'Your new List is: {user_List}')

# # WAP that reverses a list of integers (in place).
user_List = eval(input("Enter a list conatining integer elemets: "))

'''METHOD I '''  # converting to string and reversing.
for i in range(len(user_List)):
    user_List[i] = int(str(user_List[i])[::-1])
print(f"Your new reversed list is {user_List}")

'''METHOD II'''  # using reverse algorithm of integers.
for i in range(len(user_List)):
    d = 0
    while(user_List[i] != 0):
        d = d*10+user_List[i] % 10
        user_List[i] //= 10
    user_List[i] = d
print(f"Your new reversed list is {user_List}")

# # WAP asking the user to enter a list containing numbers 1 to 12. Then replace all the entries in the list that are greater than 10 with 10.
user_List = eval(
    input("Enter a list containing integer numbers between 1 and 12: "))
for i in range(len(user_List)):
    if user_List[i] > 10:
        user_List[i] = 10
print(f"Your modified list is: {user_List}")


# # WAP asking the user to enter a list of strings. Create a new list that consists of those strings with their first characters removed.
user_List = eval(input("Enter a list conatining String elements: "))
mod_List = []
for i in range(len(user_List)):
    mod_List.append(user_List[i].replace(user_List[i][0], ''))
print(f"Your Modified new List is {mod_List}")


# # WAP to check if a number is present in the list or not. If the number is present, print the position of the number. Print an appropriate message if the number is not present in the list.
user_List = eval(input("Enter a list conatining integer elements: "))
number = int(input("Enter number to check: "))
if number in user_List:
    print(f"Number is present at position {user_List.index(number)+1}")
else:
    print(f"{number} is not present in the list.")
