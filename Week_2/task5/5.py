
# Modifying a Tuple indirectly
shopping_list = ("bucket", "toothbrush","sanitory","soap","books",)
# Converting tuple to a list
lst = list(shopping_list)
lst.append("Vegetables")
lst.append("laptop")
print(lst)
# Converting back to a tuple
tuple_list = tuple(lst)
print("|".join(tuple_list))
