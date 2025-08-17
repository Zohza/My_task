# **Task2: Super Market Price List**
# - Create a program that stores items and their prices in a dictionary.

# #   - Items should come from a list.

# #   - Prices are entered by the user.

# #   - Display all items and prices, then allow the user to update the price of an item.

# # - Requirements:

# #   - Use dictionary update method `.update()` or assignment.

# #   - Use `.keys()` to display available items.

# #   - Use input validation (no advanced functions).



# Create a list of items
items = ["milo", "milk","bornvita","indomie"]

price= {}
price["milo"] =float(input("enter the price of milo: "))
price["milk"] = float(input("enter the price milk: "))
price["bournvita"] = float(input("enter the price bournvita: "))
price["indomie"] = float(input("enter the price indomie: "))
items={
 "milo": price["milo"],
 "milk":price["milk"],
"bournvita":price["bournvita"],
"indomie" : price["indomie"],}

print("\n---Initial item list---")
print(items)
print(items.keys())

# # allowing the user to update price list

choice = input("\nDo you want to update a price? (yes or no): ")
if choice == "yes":
    items_to_update = input("Enter the item you want to update: ").lower()
    if items_to_update in items.keys():
        new_price = float(input("kindly enter the new price for the selected item: "))
        items.update({items_to_update:new_price})
        print(f" You have successfully updated the price of {items_to_update}")
        print("Updated price list:", items)
if choice == "no":
    print("\nFinal price list:")
    print(items)

