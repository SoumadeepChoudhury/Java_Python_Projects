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
