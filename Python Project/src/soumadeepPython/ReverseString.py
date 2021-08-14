# Reverse a String....

s = input("Enter String: ")
sn = ""
for i in range(len(s)-1, -1, -1):
    sn += s[i]
print(sn)
