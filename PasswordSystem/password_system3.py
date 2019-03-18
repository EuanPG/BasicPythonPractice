password = ""
password_check = ""

password = input("Please enter a password.")

while password == ("huddersfield") or password == ("justinbieber") or password == ("cheese") or password == ("canalside"):
    password = input("You cannot change your password to this common password.")

while (len(password) < 6) or (len(password)> 12):
    password = input("Password must be 6-12 characters long inclusive.")

while password != password_check:
    password_check = input("Please re-enter the same password.")
print("Password Changed.")