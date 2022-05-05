# WAP that inputs a main string and then creates an encrypted string by embedding a short symbol based after each character.The program should also be able to produce the decrypt string from the encrypted string.
from random import randint
ENCKEYLIST = "!@#$%^&*()_+="
rangeStart, rangeEnd = 0, 0
while (rangeEnd <= rangeStart):
    rangeStart = randint(0, 12)
    rangeEnd = randint(0, 12)
encKey = ENCKEYLIST[rangeStart:rangeEnd]


def encrypt(string: str) -> str:
    encStr = ''
    temp = 0
    for i in range(0, len(string), 2):
        if string[i] == ' ':
            encStr += string[i]
            continue
        if i != 0:
            encStr += string[temp:i]+encKey
        temp = i
    encStr += string[temp:]+encKey
    return encStr


def decrypt(string: str) -> str:
    decStr = ''.join(string.split(encKey))
    return decStr


userInput = input("Enter user Input to encrypt: ")
print("After Encrypting: ", encrypt(userInput))
print("After Decrypting: ", decrypt(encrypt(userInput)))


# Q. Write a Python program having following functions:
# (i) A function with the following signature:
#       remove_letter (sentence, letter)
# This function should take a string and a letter (as a single-character string) as arguments returning a copy of that string with every instance of the indicated letter removed
# For example remove_letter ("Hello there!", "e") should return the string "Hllo thr!".

# (ii) Write a function to do the following :
# Try implementing the capwords () functionality using other functions, i.e , split(), capitalize () and join( ). Compare the result with the capwords() function's result.
def remove_letter(sentence: str, letter: str) -> str:
    sentence = sentence.replace(letter, '')
    return sentence


def capwords(sentence: str) -> str:
    senList = sentence.split()
    for i in range(len(senList)):
        word = ''
        for j in senList[i]:
            word += j.capitalize()
        senList[i] = word
    sentence = ' '.join(senList)
    return sentence


print("After removing desizered letter: ", remove_letter(
    input("Enter sentence: "), input("Enter letter to be removed: ")))
print("Use of Capwords function: ", capwords(
    input("Enter sentence to CAPITALISE: ")))
print("No Use of Capwords function: ", input(
    "Enter sentence to CAPITALISE: ").upper())
