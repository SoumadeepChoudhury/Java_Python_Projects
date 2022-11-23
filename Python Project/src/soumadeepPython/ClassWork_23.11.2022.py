# Stack Implementation

def isEmpty(stk:list)->bool:
    if stk==[]:
        return True
    else:
        return False

def Push(stk:list,item:str|int|float,stack_type:chr,length:int|None)->None:
    if stack_type.lower()=="b":
        if len(stk)+1>length and length is not None:
            print(f"Uncaught error occured.\nCondition: Overflow")
        else:
            stk.append(item)
    elif stack_type.lower()=="u":
        stk.append(item)
        print(f"Item {item} pushed successfully..")

    

def Pop(stk:list)->str|int|float:
    if isEmpty(stk):
        return "Underflow"
    item=stk.pop()
    return item

def Display(stk:list)->None:
    if isEmpty(stk):
        print("Stack is empty..")
    else:
        top=len(stk)-1
        print(stk[top],"<--top")
        for item in range(top-1,-1,-1):
            print(stk[item])

def Peek(stk:list)->str|int|float:
    if isEmpty(stk):
        return "Underflow"
    top=len(stk)-1
    return stk[top]




if __name__=="__main__":
    stack=[]
    stack_type=input("What kind of stack you want\nb:bounded\tu:unbounded [b/u]: ").lower()
    if stack_type=="b":
        length=int(input("Enter the length of stack: "))
    else:
        length=None
    while True:
        print("Select from the following...\n1. Push\n2. Pop\n3. Peek\n4. Display Stack\n5. Exit")
        choice=int(input("Enter your choice: "))

        if choice==1:
            item=input("Enter Item to be pushed: ")
            Push(stack,item,stack_type,length)
        elif choice==2:
            item=Pop(stack)
            if item == "Underflow":
                print(f"Uncaught error occured.\nCondition: {item}")
            else:
                print(f"Popped Item: {item}")
        elif choice==3:
            item=Peek(stack)
            if item == "Underflow":
                print(f"Uncaught error occured.\nCondition: {item}")
            else:
                print(f"Topmost Item: {item}")
        elif choice==4:
            Display(stack)
        elif choice==5:
            break
        else:
            print("Invalid Choice...")
        print(f"\n\n{'-'*20}\n\n")

