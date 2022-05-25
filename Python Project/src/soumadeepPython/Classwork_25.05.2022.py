fileInp = open("Article.txt", "a+")
fileInp.write("Hello World")
text = fileInp.read()
count = 0
for i in text:
    if i == i.upper():
        count += 1
print("Number of upper case characters: ", count)
fileInp.close()
