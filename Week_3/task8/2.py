# '''an input to enter the user's name'''
# '''input to enter the user's age, using int' for numbers'''
# '''input to enter the user's testscore, using int' for numbers'''

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))
# '''and operator to state the condition for eligibility'''
# '''defining the conditions using comparing operators "<" and ">"
# there are two conditions
# 1. age < 18
# 2. score > 70
# if both conditions are not met, the program prints False, which implies the user is ineligibility 
# if only one condition is met, the program prints FALSE, which implies that the user is ineligible
# if both conditons are met, the program prints TRUE which implies that the user is eligible'''
# eligibility = (age < 18) and (score > 70)
# ''' printing the candidates name, age, score, and eligibility, aligning it by adding each value in a new line using \n'''
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")



# Federal Government Scholarship key eligibility Requirements;
# enrollment = "Undergraduate"
# school = "Nigerian Univeristy"
name = input("Enter your name: ").title()
citizen = input("\n Are you a Nigerian?(yes/no): ").lower()
enrollment = input("\n Are you a registered, full-time undergraduate student in a recognized Nigerian university.\n(yes/no):").lower()
scholarships = input("\nAre you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international.\n(yes/no):").lower()
qualifications = input("\nDo you have five distinctions (A's and B's) in 5 core subjects: (yes/no)").lower()
# print("\nKindly input your five core subjects including Mathematics and English in this format 'Biology B' ")
# subjects = input("\nFirst subject grade: ").lower(),
# input("\nsecond subject grade: ").lower(),
# input("\nthird subject grade': ").lower(),
# input("\nfourth subject grade: ").lower(),
# input("\nfifth subject grade: ").lower()
# print (subjects)

eligibility = (citizen == "yes") and (enrollment == "yes") and (scholarships == "no") and (qualifications == "yes")
print(f"Candidate's Name: {name}\nNigerian Citizen: {citizen}\nEnrollment in a Nierian University: {enrollment}\nAcademic Qualifications: {qualifications}\nEligibility: {eligibility}")