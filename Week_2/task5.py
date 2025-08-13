# # Asking the user to enter values using tuple
# dish1 = input("Kindly Enter  of your favorite Nigerian dish: ")
# dish2 = input("second favorite Nigerian dish: ")
# dish3 = input("Third favorite Nigerian dishes: ")
# dishes = (dish1,  dish2, dish3)
# print(dishes)
# print(f"{dish1}\n{dish2}\n{dish3}")
# print(type(dishes))



# Task 2:
# Asking the user for 5 best friend's name
# names = (input("Dear user , enter your best friends' name, ensure you add comma after each name: "))
# split_names = names.split(",")
# t = tuple(split_names)
# print(t)


# print(t[::-1])

# # Task 3
# # Asking the user for 5 Nigerian states using split method
# states = input("Dear user, Kindly enter 5 Nigerian state and seperate each state with a comma: ")
# split_states = states.split(",")
# t = tuple(split_states)
# print(t)
# print(t[0])
# print(t[-1])


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













