number_of_students = int(input("Please enter the number of students."))
while number_of_students <= 0:
    number_of_students = int(input("Please enter a positive value for the number of students."))

computers_per_lab = int(input("Please enter the number of computers in each lab."))
while computers_per_lab <= 0:
    computers_per_lab = int(input("Please enter a positive value for the number of computers per lab."))

labs_needed = (number_of_students // computers_per_lab) + (number_of_students % computers_per_lab > 0)

if labs_needed == 1:
    print("You need 1 lab for all the students.")
else:
    print("You need " + str(labs_needed) + " labs for all the students.")