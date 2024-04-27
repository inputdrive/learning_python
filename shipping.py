weight = 11
# print(type(weight))

if weight <= 2:
  g_weight_cost = weight * 1.50 + 20 
  d_weight_cost = weight * 4.50
elif weight > 2 and weight <= 6:
  g_weight_cost = weight * 3.00 + 20
  d_weight_cost = weight * 9.00
elif weight > 6 and weight <= 10:
  g_weight_cost = weight * 4.00 + 20
  d_weight_cost = weight * 12.00
else:
  g_weight_cost = weight * 4.75 + 20
  d_weight_cost = weight * 14.25
print ("Here are your options ")
print ("Ground Shipping: $" + str(g_weight_cost))
print ("Drone Shipping: $" + str(d_weight_cost))
print ("Premium Shipping: $125.00")
if g_weight_cost < d_weight_cost and g_weight_cost < 125:
  print ("Ground Shipping is the cheapest option")
elif d_weight_cost < g_weight_cost and d_weight_cost < 125:
    print ("Drone Shipping is the cheapest option")
else:
    print ("Premium Shipping is the cheapest option")
# print("Ground Shipping: $" + str(g_weight_cost))