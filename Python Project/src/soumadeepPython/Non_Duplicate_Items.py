# WAP to eliminate duplicate elements in a list.

size=int(input("Enter Size of list: "))
listOfElements:list=eval(input("Enter list of elements: "))
listOfElements_copy=listOfElements.copy()
listOfNonDuplicatedElements=[];
for i in listOfElements_copy:
    if(listOfElements_copy.count(i)>1):
        listOfElements.remove(i)
        if(i in listOfElements):
            listOfNonDuplicatedElements.append(i);
    else:
        listOfNonDuplicatedElements.append(i)
print(listOfNonDuplicatedElements)