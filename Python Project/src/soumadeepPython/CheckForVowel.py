# Check For Vowel in a sentence....

s = input("Enter String: ")
s = s.lower()
f = 0
for i in range(0, len(s)):
    if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u'):
        f = 2
        break
    else:
        f = 1
if f > 1:
    print("Yes, Present")
else:
    print("No, Not Present")
