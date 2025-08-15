# create an empty set
antendees = set()
# Collect the names of people attending the seminar using .add
antendees.add("Boluwatife")
antendees.add("Eniola")
antendees.add("Fola")
antendees.add("Boluwatife")
antendees.add("Sandra")
# Convert to list to arrange them in alphabetical order
antendees_list = list(antendees)
# use the sorted method to arrange in alphabetical order
print(sorted(antendees_list))