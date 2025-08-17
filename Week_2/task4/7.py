# creating a list of 5 cities
city = ["Lagos","Ikeja","Sango","Benin","Abuja"]
# Replacing the third city with a new one entered by the user using the input fuctiona and .replace attribute
new_city = input("Enter a new city: ").title()
city.insert(2, new_city)
print(city)
# Removing the last city
city.remove("Abuja")
print(city)
# adding a new city to the begining using .insert()
new_city1 = ("Delta")
city.insert(0, new_city1)
# Printing the updated list
print(city)