# WAP accept a string and display the word which end with vowel.
userInp=input("Enter String: ")
words=userInp.split()
for i in words:
    if i[-1].upper() in ['A','E','I','O','U']:
        print(i,end=',a ')


# SMITH NUMBER.....A Smith number is a composite number whose sum of digits equals to the sum of digits of its prime factors
userinp=int(input("Enter Number: "))
temp=userinp
sum_of_number=0
Prime_factors=[]
sum_of_Prime=0
factors=1
while temp>0:
    d=temp%10
    sum_of_number+=d
    temp//=10
for _ in range(1,userinp//2):
    count_temp=1
    if userinp%factors==0:
        for k in range(1,factors):
            if factors%k==0:
                count_temp+=1
    if count_temp==2:
        Prime_factors.append(factors)
        userinp=userinp//factors
        factors=1
    else:
        factors+=1
        continue
for x in Prime_factors:
    while x>0:
        d=x%10
        sum_of_Prime+=d
        x//=10

if sum_of_Prime==sum_of_number:
    print("Smith Number")
else:
    print("Not a Smith Number..")