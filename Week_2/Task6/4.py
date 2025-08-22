
# create an empty set to store voters names
# using an input statement the user enters their name
# usinf the if and else statement
# use "if"  for detecting whether the input is already in the set, with a warning message
# use "else" for adding the user name into the set and print together with a display message
# use len method to get the number of voters


# creating an empty set
voters = set()

for i in range(1, 6):

    name = input("Enter you name: ")
    if name in voters:
        print("Multiple voting is not allowed!")
    else:
     voters.add(name)
     print("You have succesfully voted.")

print(voters)









