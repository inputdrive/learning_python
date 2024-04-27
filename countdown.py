### While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# while code below: 
count = 10
print("countdown from 10")
while count >= 0:
  print("count is " +str(count))
  count -= 1
  print("------")
print("We have liftoff!")

# while code variation below: 
countdown = 10
while countdown >= 0:
  print(str(countdown))
  countdown -= 1
print("We have liftoff!")