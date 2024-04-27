with open("logger.txt") as log_txt_file:
  print(log_txt_file.read())
# or
with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())

# reminders
# 1. Use the open() function to create a file object.
# 2. Use the .read() method to access the contents from the file object.
# 3. Don't forget to close the file object using the .close() method.
# 4. Use the with statement to ensure your file object is properly closed.
# 5. Use the .readline() method to read individual lines from the file object.
# 6. Use the .readlines() method to read all lines from the file object.
# 7. Use the .split() method to split a string into a list.
# 8. Use the .splitlines() method to split a string into a list, breaking at line boundaries.
# 9. Use the .strip() method to remove whitespace from the beginning and end of a string.
# 10. Use the .join() method to concatenate a list of strings into a single string.
# 11. Use the .write() method to write to a file object.
# 12. Use the .writelines() method to write a list of strings to a file object.
# 13. Use the .append() mode to add data to the end of a file.
# 14. Use the .seek() method to move the cursor to a specific position in the file.
# 15. Use the .tell() method to get the current position of the cursor in the file.
# 16. Use the .flush() method to clear the internal buffer of a file object.
# 17. Use the .truncate() method to remove content from a file object.
# 18. Use the .readable() method to check if a file object is readable.
# 19. Use the .writable() method to check if a file object is writable.
# 20. Use the .closed() method to check if a file object is closed.
# 21. Use the .name attribute to get the name of the file object.   
# 22. Use the .mode attribute to get the mode of the file object.
# 23. Use the .encoding attribute to get the encoding of the file object.
# 24. Use the .errors attribute to get the error handling of the file object.
# 25. Use the .newlines attribute to get the newline character of the file object.
# 26. Use the .buffer attribute to get the buffer of the file object.
# 27. Use the .detach() method to remove the underlying buffer of a file object.
# 28. Use the .readable() method to check if a file object is readable.