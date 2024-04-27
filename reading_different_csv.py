# Description: Reading a csv file with a different delimiter
import csv
with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list=[]
  for row in books_reader:
    isbn_list.append(row["ISBN"])
print(isbn_list)

# output from the csv file
['978-0-12-995015-8', '978-1-78110-100-1', '978-0-315-25137-3', '978-0-388-70665-7', '978-1-75098-721-6', '978-1-06-483628-6', '978-0-7419-8114-1', '978-1-4457-0480-7', '978-0-657-61030-2', '978-1-5039-7539-2']