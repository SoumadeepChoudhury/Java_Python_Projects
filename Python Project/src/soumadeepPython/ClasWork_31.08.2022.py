# WAP accept a string and display the word that startswith 'P'.
userInp=input("Enter string: ").lower()+" "
p=0
for i in range(0,len(userInp)):
    words=""
    if userInp[i] == ' ':
        words=userInp[p:i]
        p=i+1
    if words.startswith('p'):
        print(words)