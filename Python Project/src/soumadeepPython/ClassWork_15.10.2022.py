# Primorial Number
def primorial(num):
    if num>0:
        count=1
        for i in range(1,num):
            if num%i==0:
                count+=1
        if count!=2:
            return primorial(num-1)
        else:
            return num*primorial(num-1)
    else:
        return 1
prod = primorial(3)
if prod==1:
    print("Not a Prime Number...")
else:
    print(prod)