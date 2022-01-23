# Conversions of all binary to decimal, decimal to hexa.....etc.....

print(".....XER CALCULATOR.......\nPLEASE SELECT ANY ONE\n1.  DECIMAL  TO BINARY\n2.  BINARY TO DECIMAL\n3.  DECIMAL TO OCTAL\n4.  OCTAL TO DECIMAL\n5.  OCTAL TO BINARY\n6.  BINARY TO OCTAL\n7.  DECIMAL TO HEXADECIMAL\n8.  HEXADECIMAL TO DECIMAL\n9.  BINARY ADDITION\n10. BINARY SUBSTRACTION\n0.  EXIT")
while True:
    try:
        choice = int(input("Enter choice: "))
        if(choice == 1):  # Decimal to Binary
            userInp = int(input("Enter decimal value: "))
            print(
                f"Binary value is: {'-'+(bin(abs(userInp))[2:])  if userInp<0 else bin(userInp)[2:]}")

        if(choice == 2):  # Binary to Decimal
            userInp = input("Enter Binary value: ")
            print(
                f"Decimal value is: {(int(userInp,2))}")

        if(choice == 3):  # Decimal to Octal
            userInp = int(input("Enter decimal value: "))
            print(
                f"Octal value is: {'-'+(oct(abs(userInp))[2:])  if userInp<0 else oct(userInp)[2:]}")

        if(choice == 4):  # Octal to Decimal
            userInp = input("Enter Octal value: ")
            print(
                f"Decimal value is: {(int(userInp,8))}")

        if(choice == 5):  # Octal to Binary
            userInp = input("Enter Octal value: ")
            decimal = int(userInp, 8)
            print(
                f"Binary value is: {'-'+(bin(abs(decimal))[2:])  if decimal<0 else bin(decimal)[2:]}")

        if(choice == 6):  # Binary to Octal
            userInp = input("Enter Binary value: ")
            decimal = int(userInp, 2)
            print(
                f"Octal value is: {'-'+(oct(abs(decimal))[2:])  if decimal<0 else oct(decimal)[2:]}")

        if(choice == 7):  # Decimal to hexadecimal
            userInp = int(input("Enter Decimal value: "))
            print(
                f"Hexadecimal value is: {('-'+(hex(abs(userInp))[2:])  if userInp<0 else hex(userInp)[2:]).upper()}")

        if(choice == 8):  # Hexadecimal to Decimal
            userInp = input("Enter Hexadecimal Value: ")
            print(
                f"Decimal value is: {int(userInp,16)}")

        if(choice == 9):  # Binary Addition
            print(bin(int(input("Enter binary input 1: "), 2) +
                  int(input("Enter binary input 2: "), 2))[2:])

        if(choice == 10):  # Binary Substraction
            print(bin(int(input("Enter binary input 1: "), 2) -
                  int(input("Enter binary input 2: "), 2)).replace('0b', ''))

        if(choice == 0):
            break
    except:
        print("Ooooops!!!...GOT an ERROR...TRY AGAIN")
