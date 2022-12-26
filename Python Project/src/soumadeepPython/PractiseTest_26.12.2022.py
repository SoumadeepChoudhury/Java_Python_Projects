#Write a method in python, which will randomly generate 8 numbers and display their respective mean, median and mode.  
def mmm():
    from random import randint
    num=[]
    sumVar=0
    hashMap={}
    mode=[]
    userInputRange=int(input("Enter Number range: "))
    for i in range(0,8):
         num.append(randint(1,userInputRange))
    for j in num:
        sumVar+=j
        con=num.count(j)
        hashMap[j]=con
    maxi=max(i for i in hashMap.values())
    for i,j in hashMap.items():
        if j==maxi:
            mode.append(i)
    mode=max(mode)
    if len(num)%2==0:
        median=num[(len(num)+1)//2]
    else:
        median=num[len(num)/2]
    print("Num: ",*num)
    print("Mean: ",sumVar/len(num))
    print("Median: ",median)
    print("Mode: ",mode)

#Write a Program in python to input a expression with some brackets and check, print out if the expression is valid or not.
def valid():
    userInput=input("Enter expressions: ")
    listStack=[]
    for i in userInput:
        if i in '({[':
            listStack.append(i)
        if i in ')':
            for j in listStack:
                if j!='(':
                    _=listStack.pop()
                    continue
                listStack.pop()
                break

        if i in '}':
            for j in listStack:
                if j!='{':
                    _=listStack.pop()
                    continue
                listStack.pop()
                break
        if i in ']':
            for j in listStack:
                if j!='[':
                    _=listStack.pop()
                    continue
                listStack.pop()
                break
    if listStack==[]:
        print("Valid")
    else:
        print("Invalid")


#Write a method in Python which will display the nearest prime number.
def nearestPrime():
    userInput=int(input("Enter number: "))
    for i in range(userInput+3,userInput-11,-1):
        count=0
        for j in range(1,i):
            if i%j==0:
                count+=1
        if count==1:
            if i>userInput:
                prime=i
            else:
                if prime-userInput>userInput-i:
                    print(i)
                else:
                    print(prime)
                break



'''A binary file "Book.dat" has structure [BookNo,Book_Name,Author,Price]

 i) Write a user defined function Create_file() to input data for n records and add to Book.dat

ii) Write a function CountRec(Author) in python which accepts the Author name as parameter and count the number of books by the given Author are stored in the binary file "Book.dat".
'''

def b_file():
    def Create_file():
        import pickle
        while True:
            BookNo=input("Enter BookNo: ")
            Book_Name=input("Book Name: ")
            Author=input("Author: ")
            Price=float(input("Enter Price: "))
            data={'BookNo':BookNo,'Book Name':Book_Name,'Author':Author,'Price':Price}
            with open('Book.dat','ab') as file:
                try:
                    pickle.dump(data,file)
                except Exception as e:
                    print(e)
            if input("Do you wanna continue to enter records?[y/n]").lower()=='n':
                break
    def CountRec(auth):
        import pickle
        with open('Book.dat','rb') as file:
            data=' '
            count=0
            try:
                while data:
                    data=pickle.load(file)
                
                    if data['Author']==auth:
                        count+=1
            except:
                pass
        print(count)
    #Create_file()
    CountRec('w')


#Write a function in python ,Push(SItem) where, SItem is a dictionary conatining the details of stationary items-{Sname:price}. The function should push the names of those items in the stack who have price greater than 75. Also display the count of elements pushed into the stack.

def Push(SItem):
    for i,j in  SItem.items():
        if j > 75:
            stack.append(i)

    print(len(stack))


#Write a function LShift(Arr,n) in python, which accepts a list Arr of numbers and n is the numeric value by which all the elements of the list are shifted to left.

def LShift(Arr,n):
    for i in range(0,len(Arr)-n):
        if i-n<0:
            pos=i-n+len(Arr)
        else:
            pos=i-n
        Arr[i],Arr[pos]=Arr[pos],Arr[i]
    print(Arr)
LShift([1,2,3,4,5,6],2)
