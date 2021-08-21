'''
A positive n digit number X is called a Keith number (or repfigit number) if it is arranged in a special number sequence generated using its digits. The special sequence has first n terms as digits of x and other terms are recursively evaluated as the sum of previous n terms. For example, 197, 19, 742, 1537, etc. The program stops if the value computed is greater than the input number. 
'''

input_Number = int(input("Enter number to check for keith number: "))
series = list(str(input_Number))
sum = 0
k = 0
while(sum != input_Number):
    sum = 0
    for i in range(k, len(series)):
        sum += int(series[i])
    series.append(str(sum))
    k += 1
    if sum == input_Number:
        print("Keith Number")
    elif(sum > input_Number):
        print("Not Keith number")
        break
