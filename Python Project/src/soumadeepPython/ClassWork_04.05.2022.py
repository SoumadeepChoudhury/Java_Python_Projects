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
