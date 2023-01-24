def inputAnalyser():
    string_value = []
    integer_value = []
    float_value = []
    while True:
        userInp = input("Enter Data : ")
        if userInp.isalpha():
            string_value.append(userInp)
        else:
            if '.' in userInp:
                float_value.append(userInp)
            else:
                integer_value.append(int(userInp))
        if input("Do you wanna continue? [y/n]: ").lower() == 'n':
            break
    print("String Value", string_value)
    print("Integer Value", integer_value)
    print("Float Value", float_value)


def test():
    li = eval(input("Enter the list: "))
    li_int = []
    li_float = []
    li_str = []
    for i in li:
        if (type(i) == type(1)):
            li_int.append(i)
        elif (type(i) == type(1.5)):
            li_float.append(i)
        elif (type(i) == type('s')):
            li_str.append(i)
    print(li)
    print(li_int)
    print(li_float)
    print(li_str)
