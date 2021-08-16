# WAP that takes two strings as input and displays the smaller string in single line and the larger string as per this format...
'''
1st letter                  last letter
    2nd letter             2nd last lettter
        3rd letter      3rd last letter
                    :
'''
# PROCESS 1
user_Input1 = input("Enter 1st Text: ")
user_Input2 = input("Enter 2nd Text: ")
large = ""
if(user_Input1 < user_Input2):
    print(user_Input1)
    large = user_Input2
elif(user_Input1 > user_Input2):
    print(user_Input2)
    large = user_Input1
else:
    print("Both are equal")
k = 2
for i in range(round(len(large)/2)):
    for j in range(i):
        print(" ", end='')
    print(large[i], end='')
    for j in range(len(large)-k):
        print(" ", end='')
    k += 2
    print(large[len(large)-i-1])


# PROCESS 2
small, large = min(user_Input1, user_Input2), max(user_Input1, user_Input2)
print(small)
length = len(large)
for i in range(length//2):
    print(' ' * i + large[i] + ' ' * (length-2*(i+1)) + large[-(i+1)])
    if length % 2 == 1:
        print(' ' * (length//2) + large[length//2])
