# Write a function that tales up a number and tests if it is a prime number using recursion technique.
def test_prime(uNum,divNum=2):
    if uNum==divNum:
        return True
    if uNum%divNum==0:
        return False
    return test_prime(uNum,divNum+1)


# Implement a function product() to multiply 2 numbers recursively using + and - operators only.
def product(num,times,prod=0)->int:
    prod+=num
    if times==1:
        return prod
    return product(num,times-1,prod)



# Hailstone Number.
def hailtone(seqNum):
    if seqNum==1:
        print(seqNum)
        return
    print(seqNum,end=', ')
    if seqNum%2==0:
        return hailtone(seqNum//2)
    else:
        return hailtone((3*seqNum)+1)