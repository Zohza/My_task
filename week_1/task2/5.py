# 5
name = input("kindly enter the Market name: ").title()
traders = int(input(f"Kindly enter the number of traders in {name} market:  "))
revenue = float(input("Kindly enter the daily revenue in Naira: "))
formated_revenue = f"{revenue:,}"


# displaying the result using f-string formatting .
print(f"{name} Market has {traders} traders and generates an average revenue of {formated_revenue}")