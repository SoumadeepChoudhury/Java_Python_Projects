# # SUNDAY,MONDAY,WEDNESDAY,SATURDAY...…….n terms...
li = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY",
      "THURSDAY", "FRIDAY", "SATURDAY"]
user_Inp = int(input("Enter number of terms: "))
t = 0
d = 0
z = 1
for i in range(user_Inp):
    if(t == 21):
        t, z, d = 0, 1, 0
    t = t+d
    d = d+1
    if(t <= 6):
        print(li[t])
    else:
        print(li[t - 7*z])
        z += 1
