# WAP that inputs a main string and then creates an encrypted string by embedding a short symbol based after each character.The program should also be able to produce the decrypt string from the encrypted string.
def encrypt(string: str) -> str:
    encStr = ''
    temp = 0
    for i in range(0, len(string), 2):
        if string[i] == ' ':
            encStr += string[i]
            continue
        if i != 0:
            encStr += string[temp:i]+"#.$%"
        temp = i
    encStr += string[temp:]+"#.$%"
    return encStr


def decrypt(string: str) -> str:
    decStr = ''.join(string.split("#.$%"))
    return decStr


userInput = input("Enter user Input to encrypt: ")
print("After Encrypting: ", encrypt(userInput))
print("After Decrypting: ", decrypt(encrypt(userInput)))
