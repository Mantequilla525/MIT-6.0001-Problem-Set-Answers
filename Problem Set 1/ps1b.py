# Inputs
annualSalary = float(input("Enter annual salary:"))
portionSavedRate = float(input("Enter portion of salary saved each month, as a decimal:"))
totalCost = float(input("Enter total cost of dream home:"))
semiAnnualRaiseRate = float(input("Enter semi-annual raise, as a decimal:"))

# Variables
currentSavings = 0
portionDownPayment = 0.25
downPayment = portionDownPayment * totalCost
r = 0.04
monthlyReturn = (currentSavings * r) / 12
monthlySalary = annualSalary / 12
portionSaved = monthlySalary * portionSavedRate
months = 0

# Problem
while currentSavings < downPayment:
    months += 1

    monthlySalary = annualSalary / 12
    portionSaved = monthlySalary * portionSavedRate

    monthlyReturn = (currentSavings * r) / 12

    currentSavings = currentSavings + portionSaved + monthlyReturn

    if months % 6 == 0:
        annualSalary = annualSalary + (annualSalary * semiAnnualRaiseRate)


print('Total months to down payment:', months)
print('Total amount saved:', currentSavings)