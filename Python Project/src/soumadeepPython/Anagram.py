# Find whether anagram or not............

s = input("Enter A String: ").lower()
sn = input("Enter another String: ").lower()
c1, c2 = 0, 0
if(sorted(s) == sorted(sn)):
    print("Anagram")
else:
    print("Not Anagram")
