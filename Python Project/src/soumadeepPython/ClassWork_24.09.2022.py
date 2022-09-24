# WAP accept a string and display the word which end with vowel.
userInp=input("Enter String: ")
words=userInp.split()
for i in words:
    if i[-1].upper() in ['A','E','I','O','U']:
        print(i,end=', ')
