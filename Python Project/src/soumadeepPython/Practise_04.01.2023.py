# WRITE A  FUNCTION INDEX_LIST(L), WHERE L IS THE LIST OF ELEMENTS PASSED AS ARGUMENT TO THE FUNCTION. THE FUNCTION RETURN ANOTHER LIST NAMED 'indexList' THAT STORES THE INDICES OF ALL NON-ZERO ELEMENTS OF L.
def index_list(L):
    indexList=[]
    for i in L:
        indexList.append(L.index(i)) if i!=0 else 0
    return indexList


# WRITE A FUNCTION ALT(L) THAT WILL DISPLAY THE ALTERNATIVE ELEMENT OF A LIST OF 5.
def ALT(L):
    for i in range(len(L)):
        if i%2==0:
            print(L[i],end=' ')


''' THE ELEMENT OF LIST L IS [1,2,3]. WRITE A FUNCTION DISPLAY(L) IN SUCH A WAY THAT IT WILL DISPLAY THE ELEMENT OF LIST LIKE
                       1
                       1  2
                       1  2  3
'''
def DISPLAY(L):
    for i in range(len(L)):
        print(*L[0:i+1])

#  WRITE A FUNCTION ADD(L) WHICH WILL DISPLAY THE SUM OF THE 2ND DIAGONAL ELEMENT OF 3 BY 3 LIST.
def ADD(L):
    print(sum([L[0][0],L[0][2],L[1][1],L[2][0],L[2][2]]))

# Write a function that reads a file and display the words separated with #
def hasSep():
    with open('file.txt','r') as file:
        print(file.read().strip().replace(" ","#"))

#write a function named AMCount() that counts the occurence of A and M (including a and m) and display it.
def AMCount():
    with open('file.txt','r') as file:
        content=file.read().lower()
        print("Occurance of A:",content.count('a'))
        print("Occurance of M:",content.count('m'))

#write a method/function DISPLAYWORDS() to read lines from any text file and display the words which are less  than 4
def DISPLAYWORDS():
    with open('file.txt','r') as file:
        cont=file.read().split()
        for i in cont:
            if len(i)<4:
                print(i,end=' ')

#create a function/method named count which will count the size of the file and display it's size in bytes.
def COUNT():
    with open('file.txt','r') as file:
        print(len(file.read()))


#write a method/function that will take marks, name, roll from the user and append in the text file.
def marksAppend():
    name=input("Enter name: ")
    roll=int(input("Enter RollNo: "))
    marks=float(input("Enter Marks: "))
    with open('file.txt','a') as file:
        file.write(f'Name:{name}\nRoll:{roll}\nMarks:{marks}')


#wap that will combine each line from first file with the corresponding line with the second line. ### ERROR/BUG
def combiner():
    with open('file.txt','r') as file:
        with open('file1.txt','r+') as file1:
            final_cont=""
            try:
                while final_cont:
                    f_read=file.readline()
                    print(f_read)
                    f1_read=file1.readline()
                    print(f1_read)
                    final_cont+=f1_read+" "+f_read+"\n"
            except Exception as e:
                print(e)
            if final_cont!="":
                file1.write(final_cont)


#WAP THAT WILL MODIFY THE NAME OF THE ROLL NO. 12 AS GURNAM IN THE FILE Stu.dat.
def modify():
    import pickle
    with open('Stu.dat','wb') as file:
        while True:
            name=input("name: ")
            roll=int(input("roll: "))
            pickle.dump({'Name':name,'Roll':roll},file)
            if roll==0:
                break
    with open('Stu.dat','rb') as file:
        while True:
            try:
                print(pickle.load(file))
            except Exception as e:
                print(e)
                print('--'*20)
                break
    with open('Stu.dat','rb+') as file:
        while True:
            try:
                pos=file.tell()
                data=pickle.load(file)
                print(data)
                if data['Roll']==12:
                    data['Name']='Gurnam'
                    file.seek(pos)
                    pickle.dump(data,file)
            except Exception as e:
                print(e)
                print('--'*20)
                break
    with open('Stu.dat','rb') as file:
        while True:
            try:
                print(pickle.load(file))
            except Exception as e:
                print(e)
                break



