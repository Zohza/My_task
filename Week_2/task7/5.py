# **Task5: Contact Quick Lookup**
# - Store three names and their phone numbers in two separate tuples.

#   - Create a dictionary from them using `dict(zip(...))`.

#   - Ask the user for a name and display the corresponding number (or an error message).

# - Requirements:

#   - Use `zip()` and d`ict()` to combine tuples.

#   - Use `.get()` for safe retrieval.

#   - No loops.

# storing names with their phone numbers in tuples
names =("Bolu","Sandra","Motunrayo")
phone_no = ("09017354580","09017354599","0901735555")
# creating a dictionary form the tuple using zip
phone_book = dict(zip(names,phone_no))
print(phone_book)
# Asing the user for a name
name = input("Kindly input the name in this search tab:  ").title()
print(name)
# retrieving a number from the phonebook
number = phone_book.get(name, "Name not found")
print(number)