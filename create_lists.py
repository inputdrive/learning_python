# Your code below: 
first_names=["Ainsley","Ben","Chani","Depak"]

preferred_size=["Small", "Large", "Medium"]
preferred_size.append("Medium")

print(preferred_size)

#customer_data=[first_names,preferred_size]

customer_data=[["Ainsley","Small",True],["Ben","Large",False],["Chani","Medium",True],["Depak","Medium",False]]
print(customer_data)

customer_data[-2][-1]=False
print(customer_data)

# workaround to remove Ben from the list
# customer_data.remove(["Ben","Large",False])
# customer_data=[["Ainsley","Small",True],["Ben","Large"],["Chani","Medium",True],["Depak","Medium",False]]

# proper way to remove Ben from the list
customer_data[1].remove(False)
print(customer_data)

customer_data_final=customer_data+[["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)