# Task 4
# Asking users' for their information:
name = input("Enter your name: ")
age = input("Enter your age: ")
fav_color = input("Enter your favorit color: ")
home_town = input("Enter your hometown: ")
person = (name, age, fav_color, home_town)

# unpacking the tuple
name, age, fav_color, home_town = person

# printing each 
print("\n----User Information---")
print(f"Name\t\t\t{name}")
print(f"Age\t\t\t{age}")
print(f"Favorite Color\t\t{fav_color}")
print(f"Home Town\t\t{home_town}")
