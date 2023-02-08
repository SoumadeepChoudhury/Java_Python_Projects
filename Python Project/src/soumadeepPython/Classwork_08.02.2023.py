stk=[]
def isEmpty():
    if stk==[]:
        return True
    return False

def push_element(item):
    stk.append(item)

def pop_element():
    if isEmpty():
        return "Stack Empty"
    return stk.pop()

while True:
    ch=int(input("1. Push\n2. Pop\n3. Exit\nEnter choice"))
    if ch==1:
        userInp=eval(input("Enter details in list : "))
        if userInp[2]=="Goa":
            push_element(userInp[:2])
    elif ch==2:
        print(pop_element())
    else:
        break


