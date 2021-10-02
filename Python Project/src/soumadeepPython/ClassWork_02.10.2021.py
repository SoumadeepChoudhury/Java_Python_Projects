# # Create a function to convert Fahrenheit to Celsius & Vice versa.

def temperature(value, unit):
    conv = 0
    if(unit == 'F'):
        conv = (value-32)*5/9
        unit = 'C'
    else:
        conv = (value*9/5)+32
        unit = 'F'
    print(f"The required temp is {conv} {unit}")


temp = input(
    "Enter temperature in F/C scale (eg: 98 F or 38 C etc): ").upper().strip()
unit = temp[-1]
value = int(temp[0:len(temp)-1].strip())
temperature(value, unit)
