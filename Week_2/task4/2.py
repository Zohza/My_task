# creating an emptylist
# shopping_list = list()
# # asking the user to enter shopping items using an input statemwnt
# item1 = input("Dear user, kindlly enter your first shopping item: ")
# item2 = input("Enter your second shopping item: ")
# item3= input("Enter your third shopping item: ")
# # adding items to a list using .append
# shopping_list.append(item1)
# shopping_list.append(item2)
# shopping_list.append(item3)
# # displaying the string using print function
# print(shopping_list)


shopping_list = list()
for i in range(1, 4):
    item = input("enter your shopping item: ")
    shopping_list.append(item)
print(shopping_list)
    