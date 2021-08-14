# Remove White Spaces from a string

userInput = input("Enter a String: ")
lists = userInput.split()
newValue = ""
for i in lists:
    newValue += str(i)
print(newValue)
