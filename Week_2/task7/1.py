
#   - Use `input()` to collect details.
#   - Use dictionary operations `(dict[key] = value)` to store data.
biodata = {}
biodata["name"]= input("Enter your name: ")
biodata["age"]= input("Enter your age: ")
biodata["gender"]= input("Enter your gender: ")
biodata["courses"]=  (input("Enter your course1: "),
                     input("Enter your course2: "),
                     input("Enter your course3: "),
                      )

# converting courses into list
course_list=list(biodata["courses"])
#   - Use `print()` formatting with `\n` and `\t` for better output.
print("\n----------User Biodata---------")
print("\biodata")