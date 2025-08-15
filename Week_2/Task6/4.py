
# create an empty set to store voters names
# using an input statement the user enters their name
# usinf the if and else statement
# use "if"  for detecting whether the input is already in the set, with a warning message
# use "else" for adding the user name into the set and print together with a display message
# use len method to get the number of voters
voters = set()

voter1= input("Dear voter, kindly enter your name: ")
if voter1 in voters:
    print("Multiple voting is not allowed!")
else:
    voters.add(voter1)
    print("You have successfully registered as a voter! ")


voter2= input("Dear voter, kindly enter your name: ")
if voter2 in voters:
    print("Multiple voting is not allowed!")
else:
    voters.add(voter2)
    print("You have successfully registered as a voter! ")
    
voter3= input("Dear voter, kindly enter your name: ")
if voter3 in voters:
    print("Multiple voting is not allowed!")
else:
    voters.add(voter3)
    print("You have successfully registered as a voter! ")

        
voter4= input("Dear voter, kindly enter your name: ")
if voter4 in voters:
    print("Multiple voting is not allowed!")
else:
    voters.add(voter4)
    print("You have successfully registered as a voter! ")


    
voter5 = input("Dear voter, kindly enter your name: ")
if voter5 in voters:
    print("Multiple voting is not allowed!")
else:
    voters.add(voter5)
    print("You have successfully registered as a voter! ")


    
voter6= input("Dear voter, kindly enter your name: ")
if voter6 in voters:
    print("Multiple voting is not allowed!")
else:
    voters.add(voter6)
    print("You have successfully registered as a voter! ")

print(voters)

# printing the total number of voters
print(len(voters))
