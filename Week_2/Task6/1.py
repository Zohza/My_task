# Asking the user to display 5 favorite fruits
# Taking all the fruits in one input
fruit_input = input("Dear user, kindly enter 5 of your favorite fruits and seperate them by spaces: ")
# Split into list
fruit_list = fruit_input.split()
# Convert fruit list to a set
fruit_set = set(fruit_list)
print(fruit_set)