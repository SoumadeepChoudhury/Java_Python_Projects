# # Write a program to accept string/sentences from the user till the user enters “END” to. Save the data in a text file and then display only those sentences which begin with an uppercase alphabet.
# userInput=""
# while userInput!="END":
#     userInput=input("Enter string/sentence: ")
#     with open("tt.txt","a") as file:
#         if userInput!="END":
#             file.write(userInput+'\n')
# with open("tt.txt",'r') as file:
#     for line in file:
#         if line[0].isupper():
#             print(line)

'''Write a program CONTAINER in Python with the following specifications :
- Radius,Height # Radius and Height of Container
- Type # Type of Container
- Volume # Volume of Container
Methods
- CalVolume() # To calculate volume
# as per the Type of container
# With the formula as given below :
Type
Formula to Calculate Volume
1
3.14 * Radius * Height
3 3.14 * Radius * Height/3
- GetValue() # To allow user to enter values of
# Radius, Height and Type.
# Also, this method should call
# CalVolume() to calculate Volume
- ShowContainer() # To display Radius, Height, Type
# Volume of the Container'''
RADIUS,HEIGHT,TYPE,VOLUME=0,0,0,0
def CallVolume(Type,Radius,Height):
    global VOLUME
    if Type==1:
        VOLUME=3.14*Radius*Height
    elif Type==2:
        VOLUME=3.14*Radius*(Height/3)
def GetValue():
    Radius=int(input("Enter radius: "))
    Height=int(input("Enter Height: "))
    Type=int(input("Enter Type: "))
    CallVolume(Type,Radius,Height)
def ShowContainer():
    global RADIUS,HEIGHT,TYPE,VOLUME
    print(TYPE,RADIUS,HEIGHT,VOLUME)
GetValue()