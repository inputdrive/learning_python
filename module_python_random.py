# Import random below:
import random

# Create random_list below:
random_list=[]
random_list2=[]


# Create randomer_number below:
for i in range(5): # 5 random numbers
  random_list.append(random.randint(1,101)) # 1 to 100

for i in range(10): # 10 random numbers
  random_list2.append(random.randint(0,101)) # 0 to 100

# Print randomer_number below:
print(random_list)
print(random_list2)

random_number = random.choice(random_list)
print(random_number)