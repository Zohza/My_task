# Task 1
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"{num1} == {num2} : {num1 == num2}")


# Explaination
# num1 = 7
# num2 = 1
# num1 == num2 
# 7 is not equal to 1 which is why it would give FALSE

# print(f"{num1} != {num2}: {num1 !=  num2}")
# Explaination
# num1 = 7
# num2 = 1
# num1 != num2 # implies that num1 is not equal to num2 which would give an output of TRUE





# print(f"{num1} > {num2}: {num1 > num2}")
# Explaination
# num1 = 7
# num2 = 1
# num1 > num2 # implies that num1 is greater than num2 which would give an output of TRUE



# print(f"{num1} < {num2}: {num1 <  num2}")
# Explaination
# num1 = 7
# num2 = 1
# num1 < num2 # implies that num1 is less than num2 which would give an output of FALSE


# # three use cases where I can apply the program below

# 1.  To check if the correct bank pin has been inputted

# 2. To  check for eligibility for university admission

# 3.  To check for the number of participant in attendance and copare it to the previous attendance



# Checking if the correct bank pin has been inputed
print("\nWelcome to Union Bank!")
print("\n1.\tChecks balance\n2.\tWithdrawal")
print("Loading.......")


# password = 2001'''
user_input = {
    "1": "\nTo Check Balance,",
    "2": "Kindly enter an amount: "
}
print(user_input.get(input("\nDear Valued Customer, Enter your preferred input:")))
# ask the user to input password
user_password = 2001
password = int(input("\nEnter your password: "))
user_password == password

print(f"\nPassword: {user_password == password}")
# password = userpassord print false
