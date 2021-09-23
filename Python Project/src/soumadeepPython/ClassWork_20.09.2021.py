# # Question below
'''
Create the following lists using a for loop:
    a) A list consisting of the integers 0 through 49
    b) A list containing the squares of the interegrs 1 through 50
    c) The list1 ['a', 'b', 'ccc', 'dddd', ....] that ends withy 26 copies of the letter z
'''
list_a, list_b, list_c = [], [], []
for a in range(0, 50):       # For loop for first question
    list_a.append(a)
for b in range(1, 51):       # For loop for second question
    list_b.append(b**2)
for c in range(97, 123):       # For loop for third question
    list_c.append(chr(c)*(c-96))
print(
    f"Answer to 1st Question {list_a}\nAnswer to 2nd question {list_b}\nAnswer to 3rd Question {list_c}")


# # Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M. For instance, if L = [3, 1, 4] and M = [1, 5, 9], then N should equal [4,6,13].
N = []
L = eval(input("Enter list of element (digits): "))
M = eval(input("Enter list of element (digits): "))
if(len(L) == len(M)):
    for i in range(0, len(L)):
        N.append(L[i]+M[i])
    print(N)
else:
    print("Length of lists not equal tho perform required calculation.")


# # Write a program that rotates the element of a list so that the element at the first index moves to the second index, the element in the second index moves to the third index, etc., and the element in the last index moves to the first index.
user_List = eval(input("Enter lists of elements"))
new_List = [user_List[len(user_List)-1]]
for i in range(1, len(user_List)):
    new_List.append(user_List[i-1])
print(new_List)
