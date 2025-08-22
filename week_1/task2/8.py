name= input("kindly enter your first name: ")
distance = float(input(f"Dear {name}, How many km is it form your home to your workplace?: "))
fare = float(input("how much is the fare per km in your area?: "))
f = distance * fare
print(f"{f:.2f}")
