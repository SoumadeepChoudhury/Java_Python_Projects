# Disarium Number..Eg: 135
def disarium(number:int)->int:
    digit=number%10
    if digit==0:
        return 0
    position=len(str(number))
    return (digit**position)+disarium(number//10)

num=135
res=disarium(137)
if num==res:
    print("Disdrium..")
else:
    print("Not disarium..")


## Write a program for Triangular Number...