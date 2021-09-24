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
new_List = [user_List[-1]]
# PROCESS 1
for i in range(1, len(user_List)):
    new_List.append(user_List[i-1])
# PROCESS 2
new_List.extend(user_List)
new_List.pop(-1)

print(new_List)


# # Write a Progarm that reads the n to display nth term of fibonacci series.
series = [0, 1]
n = int(input("Enter value of n: "))
while len(series) <= n:
    series.append(series[-1]+series[-2])
print(f"The required nth term is {series[n]}")


# # Write programs as per following specifications:
''' a) Print the length of the longest
string in the list of strings str_list.
Precondition : the list will contain
at least one element.

b) L is a list of numbers. return a new list where each element is the corresponding element of list L summed with number num. '''
# ANSWER of a)
str_list = eval(input("Enter list of Strings: "))
i = 0
position = 0
length = 0
while i < len(str_list):
    if(len(str_list[i]) > length):
        length = len(str_list[i])
        position = i
    i += 1
print(f"The longest string in the list is: {str_list[position]}")


# ANSWER of b)
L = eval(input("Enter List of numbers: "))
num = int(input("Enter value of the number to be added: "))
for i in range(len(L)):
    L[i] += num
print(L)
