
basicSalary = 0
allowances = 0

basicSalary = int(input("Input Basic Salary     : "))
allowances = int(input("Input Total Allowances : "))

annualSalary = (basicSalary + allowances)*12

if annualSalary in range(0,1200001):

    incomeTax = 0

if annualSalary in range(1200000,1700001):

    incomeTax = ((annualSalary - 1200000)/12)*0.06

if annualSalary in range(1700000,2200001):

    incomeTax = (500000/12)*0.06 + ((annualSalary - 1700000)/12)*0.12

if annualSalary in range(2200000,2700001):

    incomeTax = (500000/12)*0.06 + (500000/12)*0.12 + ((annualSalary - 2200000)/12)*0.18

if annualSalary in range(2700000,3200001):

    incomeTax = (500000/12)*0.06 + (500000/12)*0.12 + (500000/12)*0.18 + ((annualSalary - 2700000)/12)*0.24

if annualSalary in range(3200000,3700001):

    incomeTax = (500000/12)*0.06 + (500000/12)*0.12 + (500000/12)*0.18 + (500000/12)*0.24 + ((annualSalary - 3200000)/12)*0.30

if annualSalary > 3700000:

    incomeTax = (500000/12)*0.06 + (500000/12)*0.12 + (500000/12)*0.18 + (500000/12)*0.24 + (500000/12)*0.30 + ((annualSalary - 3700000)/12)*0.36


netSalary = basicSalary*92/100 + allowances - incomeTax

print("Monthly Net Salary is",netSalary)