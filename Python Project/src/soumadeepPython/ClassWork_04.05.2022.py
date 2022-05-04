# WAP that inputs a main string and then creates an encrypted string by embedding a short symbol based after each character.The program should also be able to produce the decrypt string from the encrypted string.
def encrypt(string: str) -> str:
    encStr = ''
    for i in string:
        if i is ' ':
            encStr += i
            continue
        encStr += i+"#.$%"
    return encStr


def decrypt(string: str) -> str:
    decStr = ''.join(string.split("#.$%"))
    return decStr


userInput = input("Enter user Input to encrypt: ")
print("After Encrypting: ", encrypt(userInput))
print("After Decrypting: ", decrypt(encrypt(userInput)))
