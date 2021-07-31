# WAP to accept a string and display it's toggle form.
input_Text = input("Enter text: ")
print(input_Text.swapcase())


# WAP accept a string and accept a alphabet and check how many times the alphabet occurs in that string.
input_Text = input("Enter Text: ")
alpha = input("Enter alphabet to check : ")
count = 0
for i in input_Text:
    if(i == alpha):
        count += 1
print(f"Number of times the alphabet occurs: {count}")


# WAP accept a string a replace all vowels with * in the string.
input_Text = input("Enter text: ")
new_String = ''
for i in input_Text:
    if(i in 'AEIOUaeiou'):
        new_String += '*'
    else:
        new_String += i
print("New String: ", new_String)
# OR
input_Text = input("Enter text: ")
for i in input_Text:
    if(i in 'AEIOUaeiou'):
        input_Text = input_Text.replace(i, '*')
print("New String: ", input_Text)
