# # task2-6
# name = "I am learinig python as an AI developer"
# print("python" in name) 

# Number 7
name = "Boluwatife"
name_list = list(name)
name_list.reverse()
print(''.join(name_list))

# name = "      Boluwatife"
# print(name.lstrip())

# # 8
# name = "Boluwatife    "
# print(name.rstrip())

# # # 9
# askingthe user to enter an nput
text = input("Enter a sentence:   ").lower()
vowels = ("aeiou")
vowel_count= sum(map(text.count, vowels))
print("Number of Vowels:",vowel_count)


# # # 9
# # Asking the user for a sentence and print each word in a new line
# sports = input("Dear user, what is your favorite sports: ")
# output = "\n".join(sports.split())
# print(output)

# # 10
# # Converting a string to an integer using int
# number="1234"
# numbers= int(number)
# print(numbers*2)