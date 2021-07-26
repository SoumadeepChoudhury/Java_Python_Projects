# # WAP to accept a Aadhar no. and check whether aadhar no. or not.
aadhar_NO = input("Enter aadhar no= ")
if(len(aadhar_NO) == 12):
    print("Aadhar No.")
else:
    print("Not Aadhar No.")


# # WAP a number check whether divisible by 5 and 15
input_Number = int("Enter no: ")
if(input_Number % 5 == 0 and input_Number % 15 == 0):
    print("Divisible by 5 and 15.")
