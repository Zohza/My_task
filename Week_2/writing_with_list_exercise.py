# # Method 1: Using square brackets
# empty_list = []
# print(empty_list) #Output: []


# # Method 2: Using the list() constructor
# empty_list2 = list()
# print(empty_list2)


# # List of intergers

# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# #List of strings
fruits =["apple,", "banana","cherry"]
print(fruits)

# # Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)

# # From a string (each character becomes an element)
chars = list("hello")
print(chars)


my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
# print(list_from_tuple)

numbers_range = list(range(5))
print(numbers_range)

# Squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)

# Cubes of numbers 1-4
cubes = [y**3 for y in range(4)]
print(cubes)

# # Even numbers between 0-10
evens =  [x for x in range (11) if x % 2 == 0]
print(evens)

# Matrix-like list
matrix =[[1, 2], [3, 4], [5, 6]]
print(matrix)
matrix = [["a","b"]]
print(matrix)


# Accessing elememts  in a nested list
print(matrix[0])
print(matrix[0][1])

# Accessing matrix in a nested element
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])
print(matrix[0][0])
print(matrix[0][2:])
print(matrix[2][:0])
print(matrix[2][1:])
# # print(matrix[2][:2])

# print(matrix[1][::0])
# # Printing list of fruits using matrices

# Allowing duplicates with list
# items =["rice", "beans","yam","rice"]
# print(items)

# numbers = [1, 2, 3]
# numbers[1] = 20
# print(numbers)

# mixed = [10, "Nigeria", 3.14, True]
# print(mixed)

# nested_list =[[1, 2], ["a", "b"]]
# print(nested_list)
# print(nested_list[0][1])

names= ["Ada"]
names.append