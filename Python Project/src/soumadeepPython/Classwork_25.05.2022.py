# Sumita Arora Class 12

# Q6 Pg: 253
fileInp = open("Article.txt", "a+")
fileInp.write("Hello World")
text = fileInp.read()
count = 0
for i in text:
    if i == i.upper():
        count += 1
print("Number of upper case characters: ", count)
fileInp.close()

# Q9 Pg: 253


def DISPLAYWORDS():
    file = open("STORY.txt", "r")
    text = file.readlines()
    for i in text:
        i.replace("\n", "")
        for j in i:
            if len(j) < 4:
                print(j)
