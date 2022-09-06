# #1) write a function in python that will return  a pattern of Pascal's triangle and write it in a .txt file......user should input the file name as PASCAL'S.TXT and range of the pattern should be decided by the user.....
# def pascal()->str:
#     pasno=1
#     file=open("PASCAL'S.TXT",'a')
#     line=''
#     rows=int(input("Enter no of rows: "))
#     for i in range(rows):
#         line+=(" "*(rows-i))
#         if i==0:
#             line+=str(pasno)+'\n'
#             pasno=11
#         else:
#             for k in range(len(str(pasno))):
#                 line+=str(pasno)[k]+" "
#             line+='\n'
#             pasno=pasno*11
#     file.write(line)
#     return (line+'\nSuccessfully Added in file')


# #2) WAP that will generate all the numbers of 4 digit... from 0 to 9 ........all the numbers will get stored in the "COLLECTOR" db table with sl no ..ND when all the numbers get stored in the db then print in the shell.  "PROGRAMS TERMINATES AFTER N SECONDS"  with the total numbers that get stored in the database table..
# import mysql.connector
# from random import shuffle   #optional
# import time
# start=time.time()
# mydb = mysql.connector.connect(
#   host="hostname",
#   user="username",
#   password="password",
#   database="databasename"
# )
# mycursor = mydb.cursor()
# if mydb:
#     query="create table if not exists Chlgn2(Slno int(4) primary key AUTO_INCREMENT,Num int(4));"
#     mycursor.execute(query)
#     numList=[]
#     for i in range(1000,10000):
#         numList.append(i)
#     shuffle(numList)   #optional
#     for i in numList:
#         query=f"insert into Chlgn2(Num) values({i})"
#         mycursor.execute(query)
#         mydb.commit()
#     end=time.time()
#     print(f"PROGRAMS TERMINATES AFTER {end-start} SECONDS")
# else:
#     print("Failed to connect. Try again later")



#3) Write a function that will transpose the element of 2-D list of 3 by 3.... and DISPLAY the 2-D list in MATRIX FORMAT...
def transpose():
    userList=eval(input("Enter 2-D list of 3x3"))
    outputList=[]
    temp=[]
    for i in range(0,len(userList)):
        temp=[]
        for itemSet in userList:
            temp.append(itemSet[i])
        outputList.append(temp)
    for i in range(0,len(outputList)):
        print(outputList[i])
transpose()