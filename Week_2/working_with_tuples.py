# Using parentheses
# example 1: Tuples with multiple items
# fruits = ("apple","banana","cherry")
# print(fruits)

# numbers = 1, 2, 3
# print(numbers)

# single_item = ("apple",)
# print(single_item)
# print(type(single_item))

# Using the tuple constructor
# fruits_list = ["apple", "banana", "cherry"]
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)

# Ordered
# colors = ["red","green","blue"]
# print(colors[0])

# # Immutable ( uncomment and run. This will cause an error)
# colors = ("red","green","blue")
# colors[1]= "yellow"
# print(colors)

# Allow duplicates
# numbers = (1, 2, 2, 3)
# print(numbers)

# Mixed data types
# mixed = (("a", "b",),(1, 2))
# print(mixed)

# Nested tuples
# nested = (("a", "b"), (1, 2))
# print(nested)


# Indexing
# fruits = ("apple", "banana", "cherry", )
# print(fruits[1])
# print(fruits[-1])

# Slicing
# print(fruits[0:2])
# print(fruits[::-1])
# print(fruits[0:2])

# 3. Concatenation
# tuple1 = (1, 2)
# tuple2 = (3, 4)
# result = tuple1 + tuple2
# print(result)

# 4. Repition
# nums = ("a", "b")
# print(nums * 3)


# nums = (1, 2)
# print(nums * 3)

# nums = (1, 2)
# print(nums * 3)

# 5. Membership
# fruits = ("apple", "banana", "cherry",)
# print("banana" in fruits)
# print("grape" not in fruits)

# 6. Iteration
# for x in fruits:
#     print(x)

# dont count() and dot index()
# numbers = (1, 2, 2, 3, 4)

# print(numbers.count(2))
# print(numbers.index(3))

# Tuple to list
# t = (1, 2, 3)
# lst = list(t)
# lst.append(4)
# print(lst)

# names = ("Bolu", "Temi")
# listed_names = list(names)
# listed_names.append("Miracle")
# print(listed_names)


# List back to Tuple
# t = tuple(lst)
# print(t)

# Built in function with Tuples
nums = (4, 1, 7, 3)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))

