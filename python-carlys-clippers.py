hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
    total_price += price
print("Total Price: " + str(total_price))

average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]
print("new haircut prices: ", new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str(average_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print("Cuts under $30: ", cuts_under_30)
# Output:   Total Price: 255
#           Average Haircut Price: 31.875
#           new haircut prices:  [25, 20, 35, 15, 15, 30, 45, 30]
#           Total Revenue: 1085
#           Average Daily Revenue: 155.0
#           Cuts under $30:  ['bouffant', 'pixie', 'crew', 'bowl']
# Path: python-carlys-clippers.py
