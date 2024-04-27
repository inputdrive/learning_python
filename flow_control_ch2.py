# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent
print("Total expenses: " + str(total))

if total > budget:
  over_budget = True
else:
  over_budget = False

# Check if the total is greater than the budget and store the result in over_budget
# over_budget = total > budget
print("Is it over budget? " + str(over_budget))

# Uncomment the below lines to see the results

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))
