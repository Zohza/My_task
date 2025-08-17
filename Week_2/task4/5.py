#  asking each user for 3 student names
name= []
score=[]
student_name1 = input("Enter your name:  ")
score1 =int(input("Enter your score:"))
student_name2 = input("Enter your name:  ")
score2 =int(input("Enter your score:"))
student_name3 = input("Enter your name:  ")
score3 =int(input("Enter your score:"))

# storing the name to the empty list
name.append(student_name1)
name.append(student_name2)
name.append(student_name3)
# storing the score to the empty list
score.append(score1)
score.append(score2)
score.append(score3)
print("-----Student Score list--------")
print(f"\n{student_name1}-----{score1}")
print(f"\n{student_name2}-------{score2}")
print(f"\n{student_name3}-------{score3}")