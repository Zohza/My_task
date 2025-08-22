# 12. Simulated USSD Menu Interaction
#  - You are to design a mock USSD interface for a mobile service.
#  - Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction.

# # Welocome greeting using a print statement
# print("Welcome my country pipu, How Una dey?! I bring greetings form the surest Ogboge Network.  ")

# Asking the user to dail the code


data_purchased = []
airtime_purchased = []


code = input("Dear User, Kindly dial the code *123#: ")
if code == "*123#":
    while True:
        print("\n1.\tCheck Balance\n2.\tBuy Data\n3.\tBuy Airtime\n4.\tExit")
        choice = int(input("Kindly choose an option: "))
        balance =10000
        choices =[ [1,"check balance"],[2,"Buy Data"],[3,"Buy Airtime"]]

        if choice == 1:
            print(f"You have selected the {choices[0][1]} option")
            print(f"Your current balance is {balance}")
        elif choice == 2:
            print(f"You have selected the {choices[1][1]} option")
            data = float(input("Kindly input the amount you want to buy: "))
            data_purchased.append(data)
            print(f"you have successfully purchased {data} amount of Data.")
        elif choice == 3:
            print(f"You have selected the {choices[2][1]} option")
            airtime = float(input("Kindly input the amount you want to buy: "))
            airtime_purchased.append(airtime)
            print(f"you have successfully purchased {airtime} amount of Data.")
        elif choice == 4:
            break
    print(f"This are the summaries of your transactions\nData Amount Purchased:\t{sum(data_purchased)}\nAirtime Purchased:\t{sum(airtime_purchased)}")
    print("Thank you for using MTN!")
        
        
    
else:
    print("Invalid Input!")
