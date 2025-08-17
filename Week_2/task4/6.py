# Asking the user to input a word using a word
word = input("Enter a word: ")
# printing the length of the word
print(len(word))
# checking if it is all uppercase, all lowercase or title case
# for uppercase
if word.isupper():
    print("Yes!, it is all in uppercase.")

# for lowercase
if word.islower():
    print("Yes!, it is all in lowercase.")

# for titlecase
if word.istitle():
    print("Yes!, it is all in titlecase.")
# Reversing the word using slicing
print(word[::-1])