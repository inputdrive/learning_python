#Write your function here
def odd_indices(my_list):
  return [my_list[i] for i in range(1, len(my_list), 2)]

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))