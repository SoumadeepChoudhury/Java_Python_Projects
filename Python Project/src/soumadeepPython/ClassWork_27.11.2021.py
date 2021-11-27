# # WAP to accept a number and display all the factors which are prime ( prime factors)
user_Inp = int(input("Enter number: "))
for i in range(1, user_Inp+1):
    c = 0
    if(user_Inp % i == 0):
        for j in range(1, i+1):
            if(i % j == 0):
                c += 1
        if(c <= 2):
            print(i, end=' ')
