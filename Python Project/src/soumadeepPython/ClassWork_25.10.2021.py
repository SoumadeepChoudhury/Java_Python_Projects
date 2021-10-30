# # # Print the series 1,-4,7,-10....-40
# k = 1
# for i in range(1, 41, 3):
#     print(i*k, end=" ")
#     k *= -1


# # WAP accept a sentence and display a word formed by each first letter of the sentence.
userInp = input("Enter a sentence: ")
newWord = userInp[0]
for i in range(0, len(userInp)):
    if userInp[i] == " ":
        newWord += userInp[i+1]
print(newWord)
