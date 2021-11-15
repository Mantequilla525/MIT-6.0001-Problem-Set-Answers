# Input ----------------------------------------------------------------
startingSalary = input("Enter the starting salary: ")
# Run a quick try/except to make sure that what the user entered
# can be converted into a float.
try:
    startingSalary = float(startingSalary)
except:
    print('Starting salary was invalid, please enter a numeric value')
    quit()


# Variables ------------------------------------------------------------
totalCost = 1000000
downPayment = totalCost * 0.25
returnRate = 0.04
monthlyReturnRate = returnRate / 12
semiAnnualRaise = 0.07
monthsToDownPayment = 36

# Binary search variables ---------------------------------------------
steps = 0
high = 10000
low = 0
bestPortion = (high + low) / 2
epsilon = 100


# Problem -------------------------------------------------------------
# The problem wants us to run a bisection (binary) search to figure out
# what the best savings rate is for 36 months. We will just run a basic
# while loop and break out of it when we find our number. For each loop
# it will go through 36 months at a given rate, and then if that rate
# isn't within epsilon, it will reset with a new rate.

while True:
    # Since this will run every time the while loop resets, we can put
    # the counter for the binary search right here at the top.
    steps = steps + 1

    # Initializing variables back to their starting values to reset them
    # on each iteration. The reason that we divide by 10000 is because we
    # are running the search using high integers. Imagine each integer
    # as a penny. By running it like this, we will only check once for each
    # "penny", or once for each place in the 0.00 decimal spot. This can
    # be very confusing, but it is not the main focus of this assignment.
    currentSavings = 0.0
    annualSalary = startingSalary
    monthlySalary = annualSalary / 12
    monthlyDeposit = monthlySalary * (bestPortion / 10000)

    # To calculate how much money we would end up saving at a given rate,
    # we will run a for loop 36 times since that is how many months they
    # have set the problem at. We start at 1, because if we started
    # at month 0 there would be a raise on the first month.
    for month in range(1, monthsToDownPayment + 1):
        # First, we add our current savings and deposit for the month
        currentSavings = currentSavings * (1 + monthlyReturnRate)
        currentSavings = currentSavings + monthlyDeposit

        # For semi annual raises, we will do the same thing we did
        # for ps1b.py by checking the remainder of what month we're on.
        if month % 6 == 0:
            annualSalary = annualSalary * (1 + semiAnnualRaise)
            monthlySalary = annualSalary / 12
            monthlyDeposit = monthlySalary * (bestPortion / 10000)

    print("Step", steps, " Savings:", currentSavings)
    # This checks if we're over our savings amount by subtracting
    # the savings amount by the down payment. If it's more than
    # our epsilon, then we must be over.
    if (currentSavings - downPayment) > epsilon:
        print('Rate:', bestPortion / 10000, ' Over')
        high = bestPortion

    # This basically just does the opposite of what the above check
    # does. It takes the savings from the down payment, and if we're
    # still above our epsilon, we must be under.
    elif (downPayment - currentSavings) > epsilon:
        print('Rate:', bestPortion / 10000, ' Under')
        low = bestPortion


    # We use absolute here because sometimes the difference between
    # savings and down payment will be negative, and we only care
    # about the actual difference between them. If the difference
    # is less than our epsilon, then we have found our number :)
    if abs(currentSavings - downPayment) < epsilon:
        print('Savings rate found! ---------------------')
        break
    
    # If we have not found our number, then we set the portion that
    # we're going to try next to halfway through the last two numbers.
    bestPortion = int((high + low) / 2)


# Remember to print out the portion as a decimal by dividing it
# by 10000!
print('Best portion saved:', bestPortion / 10000)
print('Steps in binary search:', steps)
