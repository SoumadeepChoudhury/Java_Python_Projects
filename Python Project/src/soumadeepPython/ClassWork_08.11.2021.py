# # WAP accept 10 elements in a tuples. Display perfect square elements of the tuple.
from math import pow as p
user_Inp = tuple()
for _ in range(5):
    user_Inp += (int(input("Enter elements: ")),)
for i in range(5):
    if(p(user_Inp[i], 0.5) == int(p(user_Inp[i], 0.5))):
        print(f"{user_Inp[i]} is perfect square number")

# # WAP accept a no. & check whether pronic or not.
user_Inp = int(input("Enter a no: "))
for i in range(user_Inp//2):
    if(i*(i+1) == user_Inp):
        print(f"{user_Inp} is a pronic number")
        break
else:
    print("Not a pronic number")

# # WAP accept a number and reverse the no. without using % and reverse function.
user_Inp = int(input("Enter number: "))
s = 0
while(user_Inp > 0):
    x = user_Inp//10
    f = x*10
    r = user_Inp-f
    s = s*10+r
    user_Inp //= 10
print(s)
