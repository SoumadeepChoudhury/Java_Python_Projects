# write a function in python that will return  a pattern of Pascal's triangle and write it in a .txt file......user should input the file name as PASCAL'S.TXT and range of the pattern should be decided by the user.....
def pascal()->str:
    pasno=1
    file=open("tt.TXT",'a')
    line=''
    rows=int(input("Enter no of rows: "))
    for i in range(rows):
        line+=(" "*(rows-i))
        if i==0:
            line+=str(pasno)+'\n'
            pasno=11
        else:
            for k in range(len(str(pasno))):
                line+=str(pasno)[k]+" "
            line+='\n'
            pasno=pasno*11
    file.write(line)