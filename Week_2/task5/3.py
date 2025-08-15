# # Task 3
# Asking the user for 5 Nigerian states using split method
states = input("Dear user, Kindly enter 5 Nigerian state and seperate each state with a comma: ")
split_states = states.split(",")
t = tuple(split_states)
print(t)
print(t[0])
print(t[-1])
