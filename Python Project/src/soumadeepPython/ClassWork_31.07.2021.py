# # WAP to accept a string and display it's toggle form.
input_Text = input("Enter text: ")
print(input_Text.swapcase())


# # WAP accept a string and accept a alphabet and check how many times the alphabet occurs in that string.
input_Text = input("Enter Text: ")
alpha = input("Enter alphabet to check : ")
count = 0
for i in input_Text:
    if(i == alpha):
        count += 1
print(f"Number of times the alphabet occurs: {count}")


# # WAP accept a string a replace all vowels with * in the string.
input_Text = input("Enter text: ")
new_String = ''
for i in input_Text:
    if(i in 'AEIOUaeiou'):
        new_String += '*'
    else:
        new_String += i
print("New String: ", new_String)
# # # # OR
input_Text = input("Enter text: ")
for i in input_Text:
    if(i in 'AEIOUaeiou'):
        input_Text = input_Text.replace(i, '*')
print("New String: ", input_Text)


# # # HOMEWORK
# # Write a user defined function to convert a string with more than one word into title case string where string is passed as parameter. (Title case means that the first letter of each word is capitalised)
def alter_Case(text):
    text = text.title()
    return text


text = input("Enter text: ")
print(alter_Case(text))


# # Write a function deleteChar() which takes two parameters one is a string and other is a character. The function should create a new string after deleting all occurrences of the character from the string and return the new string.
def deleteChar(text, chr):
    return text.replace(chr, '')


text = input("Enter text: ")
chr = input("Enter character to delete: ")
print(deleteChar(text, chr))


# # Input a string having some digits. Write a function to return the sum of digits present in this string.
def sum_Digits(text):
    sum = 0
    for i in text:
        if(i.isdigit()):
            sum += int(i)
    return sum


text = input("Enter text having some numbers: ")
print(sum_Digits(text))


# # Write a function that takes a sentence as an input parameter where each word in the sentence is separated by a space. The function should replace each blank with a hyphen and then return the modified sentence.
def replace(text):
    return text.replace(" ", '-')


text = input("Enter text sentence: ")
print(replace(text))
