password = input("Please enter a password.")
password_check = ""

while password != password_check:
    password_check = input("Please re-enter the same password.")
print("Password Changed.")