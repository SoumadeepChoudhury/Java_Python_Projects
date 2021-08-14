# # WAP accept a word and display the word in reverse order
word = input("Enter word: ")
for i in range(0, len(word)):
    print(word[len(word)-1-i], end='')

# # WAP accept a word and count no. of vowel in that word and display.
word = input("Enter word: ").lower()
count = 0
for i in word:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        count += 1
        print("The Vowels are: ", i)
print("Total vowels: ", count)


# # HOMEWORK.
# # Write a program to input line(s) of text from the user until enter is pressed. Count the total number of characters in the text(including white spaces), total number of alphabets, total number of digits, total number of special symbols and total number of words in the given text. (Assume that each word is separated by one space).
text = input("Enter text: ")
total_Characters = len(text)
total_Alpha, total_Digits, total_Specialsymbols, total_Words = 0, 0, 0, 0
text += " "
for i in text:
    if(i.isalpha()):
        total_Alpha += 1
    if(i.isdigit()):
        total_Digits += 1
    if(i.isalnum() == False):
        total_Specialsymbols += 1
    if(i == " "):
        total_Words += 1

print("Total Characters in the text: ", total_Characters)
print("Total Alphabets in the text: ", total_Alpha)
print("Total Digits in the text: ", total_Digits)
print("Total Special Sysmbols in the text: ", total_Specialsymbols-1)
print("Total words in the text: ", total_Words)
