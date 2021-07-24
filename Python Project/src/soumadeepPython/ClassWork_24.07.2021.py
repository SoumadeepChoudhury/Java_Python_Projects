# # WAP accept a word and count number of 'A' letter in that word.
input_Text = input("Enter a text sentence: ")
count = 0
for i in input_Text:
    if(i == 'A' or i == 'a'):
        count += 1
print("Total 'A' in text: ", count)


# # WAP accept a string and a searching word and display the index number where the word is in the string.
input_Text = input("Enter text sentence: ")
input_Search = input("Enter a searching word: ")
index_Count = input_Text.find(input_Search)
if(index_Count > -1):
    print(
        f"The word is found at index {index_Count} of the string \" {input_Text} \"")
else:
    print("Not Found")


# # WAP to print 0,5,10,15,20....till enter -1
