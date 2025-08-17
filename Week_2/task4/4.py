# Asking the user for five names seperated by a space and converting to lowercase
names = input("Dear User, Kindly input 5 names seperated by a space: ").lower()
# seperating the names using split()into a list of names
n= names.split()
print(sorted(n))