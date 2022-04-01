# WAP that prompts for a phone number of 10 digits and two dashes,with dashes after the area code anf the next three numbers. For eg: 017-555-1212 is a legal input. Display if the phone number entered is valid format or not and display if the phone nummber is valid or not(i.e.,constains just the digits and dash at specific place)
userPhone = input("Enter Phone Number: ")
if len(userPhone) == 12 and userPhone[3] == userPhone[7] == '-' and userPhone.replace('-', '').isdigit():
    print("Valid Format.")
else:
    print("Invald Format")


# WAP that should prompt the user to type some sentence(s) followed by "enter".It should then print the original sentence(s) and the following statistics relating to the sentence(s): Number of Word,Number of characters(including white-space and punctuation) and percentage of characters that are alpha numeric
userInp = input("Enter sentences: ")
print(userInp)
print(len(userInp.split(' ')))
print(len(userInp))
count = 0
for i in userInp:
    if i.isalnum():
        count += 1
print((count/len(userInp))*100)


# WAP that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding elements in L and M.
L = eval(input("Enter first list: "))
M = eval(input("Enter second list: "))
N = []
if len(L) == len(M):
    for i in range(0, len(L)):
        N.append(L[i]+M[i])
print(N)


# WAP that rotates the elements of a list so that elements at the first index moves to the second index,elements at the second index moves to the third index,....,elements at the last index moves to the first index.
userList = eval(input("Enter a list: "))
tempVar = userList[-1]
for i in range(len(userList)-1, 0, -1):
    userList[i] = userList[i-1]
userList[0] = tempVar
print(userList)


# WAP that prints the longest word in a list of words.
userList = eval(input("Enter list of words: "))
temp, word = 0, ''
for i in userList:
    if len(i) > temp:
        temp = len(i)
        word = i
print(word)
