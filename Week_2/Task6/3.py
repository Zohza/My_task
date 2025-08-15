# storing 1 to 50 seat number in a set using range
seats = set(range(1,51))
# asking the user to book a seat ny entering a number using inp
user_seat =int(input("Dear user, Kindly book a seat by entering your preferred seat number: "))
# store the input in a set
user_seat_set = {user_seat}
# remove booked seats and print the remainging
print(seats.difference(user_seat))
