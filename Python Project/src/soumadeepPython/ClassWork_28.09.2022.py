# Disply Electric Bill..
units=int(input("Enter no. of units consumed.."))
bill=0
if units<=102.00:
    bill=units*5.53
elif units>102.00 and units<=180.00:
    bill=(102.00*5.53)+((units-102.00)*6.20)
elif units>180.00 and units<=300.00:
    bill=(102.00*5.53)+(78*6.20)+((units-198)*7.20)
elif units>300.00 and units<=600.00:
    bill=(102.00*5.53)+(78*6.20)+(120*7.20)+((units-318.00)*7.54)
elif units>600.00 and units<=900.00:
    bill=(102.00*5.53)+(78*6.20)+(120*7.20)+(300*7.54)+((units-618.00)*7.81)
elif units>900.00:
    bill=(102.00*5.53)+(78*6.20)+(120*7.20)+(300*7.54)+(300*7.81)+((units-376)*9.22)
print("Your amount is :",bill)