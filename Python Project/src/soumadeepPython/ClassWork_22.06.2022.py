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
class CONTAINER:
    def __init__(self) -> None:
        self.RADIUS,self.HEIGHT,self.TYPE,self.VOLUME=0,0,0,0
    def CallVolume(self,Type,Radius,Height):
        if Type==1:
            self.VOLUME=3.14*Radius*Height
        elif Type==2:
            self.VOLUME=3.14*Radius*(Height/3)
        self.ShowContainer()
    def GetValue(self):
        self.RADIUS=int(input("Enter radius: "))
        self.HEIGHT=int(input("Enter Height: "))
        self.TYPE=int(input("Enter Type: "))
        self.CallVolume(self.TYPE,self.RADIUS,self.HEIGHT)
    def ShowContainer(self):
        print(self.TYPE,self.RADIUS,self.HEIGHT,self.VOLUME)
Object = CONTAINER()
Object.GetValue()