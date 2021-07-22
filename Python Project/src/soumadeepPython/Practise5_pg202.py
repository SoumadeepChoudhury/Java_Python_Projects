# Calculate SI AND CI


principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter Time in years: "))

si = (principal*rate*time)/100
ci = principal*((1+rate/100)**time)-principal

print("Simple Interest: ", si)
print("Compound Interest: ", ci)
