# Your code below:
toppings=["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices=[2,6,1,3,2,7,2]
num_two_dollar_slices=prices.count(2)
print(num_two_dollar_slices)

num_pizzas=len(toppings)
print(num_pizzas)

print("We sell "+str(num_pizzas)+" different kinds of pizza!")

pizza_and_prices=[prices,toppings]
pizza_and_prices=prices,toppings
print(pizza_and_prices)