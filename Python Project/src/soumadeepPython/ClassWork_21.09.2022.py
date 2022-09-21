# Armstrong number of any order.
import math
user_inp=int(input("Enter No: "))
tem_var=user_inp
count=len(str(user_inp))
addVal=0
tem_var=user_inp
while tem_var>0:
    d_=tem_var%10
    tem_var//=10
    addVal=addVal+int(math.pow(d_,count))
if addVal==user_inp:
    print("Armstrong Number")
else:
    print("Not Armstrong Number...")

# Check for Amicable Number
userinp1=int(input("Enter No.1 : "))
userinp2=int(input("Enter No.2 : "))
sum1=0
sum2=0
if userinp1>userinp2:
    temp1=userinp1
    temp2=userinp2
else:
    temp1=userinp2
    temp2=userinp1
for i in range(1,temp1//2+1):
    if temp1%i==0:
        sum1+=i
    if temp2%i==0:
        sum2+=i
if sum1==temp2 and sum2==temp1:
    print("Amicable Number")
else:
    print("Not Amicable Number...")