# # Create a function to convert fahrenheit to celcius & Vice versa.

def temperature(value, unit):
    conv = 0
    if(unit == 'F'):
        conv = (value-32)*5/9
    else:
        conv = (value*9/5)+32
    print(f"The required temp is {conv}")


temp = input("Enter temperature in F/C scale: ").strip()
unit = temp[-1]
value = int(temp[0:len(temp)-2])
temperature(value, unit)
