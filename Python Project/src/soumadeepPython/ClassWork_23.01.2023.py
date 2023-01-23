string_value=[]
integer_value=[]
float_value=[]
while True:
    userInp=input("Enter Data : ")
    if userInp.isalpha():
        string_value.append(userInp)
    else:
        if '.' in userInp:
            float_value.append(userInp)
        else:
            integer_value.append(int(userInp))
    if input("Do you wanna continue? [y/n]: ").lower() == 'n':
        break
print("String Value",string_value)
print("Integer Value",integer_value)
print("Float Value",float_value)
