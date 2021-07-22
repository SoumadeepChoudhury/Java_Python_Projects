# Palondrome Check.....

s = input("Enter String: ")
s = s.lower()
sn = ""
for i in range(len(s)-1, -1, -1):
    sn += s[i]
if(s == sn):
    print("Palindrome")
else:
    print("Not Paloindrome")
