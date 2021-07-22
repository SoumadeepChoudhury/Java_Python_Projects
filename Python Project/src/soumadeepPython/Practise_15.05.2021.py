# WAP accept basic salary of an employee where DA=10% of basic, HRA=12% of basic, PF=7.5% of basic and MA=8% of basic. Then display gross salary and net salary of the employee.


basic = float(input("Enter basic pay: "))
da = 10/100*basic
hra = 12/100*basic
pf = 7.5/100*basic
ma = 8/100*basic


gross_salary = basic+da+hra+ma
net_salary = gross_salary-pf

print("Gross Salary: ", gross_salary)
print("Net Salary: ", net_salary)
