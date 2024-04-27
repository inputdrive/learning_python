
import codecademylib3_seaborn
import random
from matplotlib import pyplot as plt

# Add your code below:
# create var
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)
print(numbers_a)
print(numbers_b)
plt.show()