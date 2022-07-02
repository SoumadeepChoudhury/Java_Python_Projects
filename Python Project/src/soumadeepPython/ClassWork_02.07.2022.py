# # Program in python to type text in a file till ~ is pressed as rightmost character.
# file=open("file.txt","a")
# while True:
#     fileinput=input("Enter text: ")
#     if fileinput.endswith('~'):
#         file.write(fileinput)
#         break
#     else:
#         file.write(fileinput)
# file.close()

# # WAP to read first 5 lines from the text file.
# file=open("file.txt")
# for i in range(5):
#     print(file.readline())

# WAP to combine each line from first file with the corresponding line of second file.
file1=open("tt.txt")
file2=open("tt1.txt")
string=" "
#Method 1
for i,j in file1,file2:
    print(i.replace("\n","")+" "+j.replace("\n",""))
#Method 2
while string:
    string=file1.readline().replace("\n","  ")
    string+=file2.readline().replace("\n"," ")
    print(string)