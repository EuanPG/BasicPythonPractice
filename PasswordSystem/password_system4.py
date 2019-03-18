password = ""
password_check = ""
username = input("Please enter username: ")
studentID = input("Please enter studentID: ")

password = input("Please enter a password: ")

while password == "huddersfield" or password == "justinbieber" or password == "cheese" or password == "canalside":
    print("You cannot change your password to this common password.")
    password = input("Please enter another password.")

while password == username or studentID:
    print("You cannot change your password to your username or studentID number.")
    password = input("Please enter another password.")

while (len(password) < 6) or (len(password) > 12):
    print("Password must be 6-12 characters long inclusive.")
    password = input("Please enter another password.")

while password != password_check:
    password_check = input("Please re-enter the same password.")
print("Password Changed.")