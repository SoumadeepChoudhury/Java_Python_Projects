# Disarium Number..Eg: 135
def disarium(number:int)->int:
    digit=number%10
    if digit==0:
        return 0
    position=len(str(number))
    return (digit**position)+disarium(number//10)



# Write a program for Triangular Number...
def triangularNum(value:int,num:int=1,prevValue:int=0)->int:
    if prevValue==value:
        return value
    prevValue=prevValue+num
    return triangularNum(value,num+1,prevValue)