name = input("Dear Customer, kindly enter your full name: ").title()
units = int(input("Enter the units  of electricity consumed "))
cost = float(input("Enter the cost per unit:  "))
total_bill = cost * units
print("\n        RECIEPTS")
print(f"\nCustomer's Name:\t{name}\nUnits Consumed:\t\t{units}\nCost per Unit:\t\t{cost}\nTotal cost:\t\t{total_bill}")
