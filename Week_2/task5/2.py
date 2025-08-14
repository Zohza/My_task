# Task 2:
# Asking the user for 5 best friend's name
names = (input("Dear user , enter your best friends' name, ensure you add comma after each name: "))
split_names = names.split(",")
t = tuple(split_names)
print(t)
print(t[::-1])
