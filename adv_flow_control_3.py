def combine_sort(my_list1, my_list2):
  unsorted = my_list1 + my_list2
  sortedList = sorted(unsorted)
  return sortedList
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))