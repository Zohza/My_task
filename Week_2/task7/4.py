# **Task4: Unique Members Registration**
# - Ask the user to enter three names separated by commas.
names = input("Enter three names seperated by commas: ").title()
#    - Convert them to a set to ensure uniqueness.
uniquenames = set(names.split(","))
print(uniquenames)

#    - Create a dictionary where each name is a key and its length is the value.
d = { name: len(name) for name in uniquenames}
print(d)

