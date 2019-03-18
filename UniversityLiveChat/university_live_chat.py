import sys
import random
email = input("Please enter your University of Poppleton email.")
domain = "pop.ac.uk"
domain_count = len(domain) + 1
email_count = len(email) - int(domain_count)

def validate_email(email, domain):

    while email.count('@') != 1:
        sys.exit("Domain invalid: Domain must include a single '@' only.")
    while domain not in email:
        sys.exit("Domain invalid: incorrect domain name.")
    while domain > str(email.split('@')[-1]):
        sys.exit("Domain invalid: domain must be after '@' symbol.")
    email_count = len(email) - int(domain_count)
    while email_count <= 0:
        sys.exit("Email invalid: email must contain text before the '@' symbol. ")

    print("Email is valid.")

validate_email(email, domain)

names_list = ("Euan", "Danny", "Tony", "Molly", "Nichola", "Katie")
student_name = email.split('@')[0]
words_list = ("Maybe", "Tell me more", "I am please to hear that")

print("Hello " + student_name + " my name is " + random.choice(names_list) + ". I am your operator, what can I help you with?")
user_input = ""
random.randint(0, 99)
while user_input != "Goodbye".lower():
    user_input = input("").lower()
    if "library".lower() in user_input:
        print("The library is closed today.")
        int(random.random()*100)
        if int(random.randint) < int(15):
            sys.exit("System has disconnected.")
        else:
            continue
    elif "WiFi".lower() in user_input:
        print("WiFi is excellent across the campus.")
        if random.randint < 15:
            sys.exit("System has disconnected.")
        else:
            continue
    elif "Deadline".lower() in user_input:
        print("Your deadline has been extended by two working days.")
        if random.randint < 15:
            sys.exit("System has disconnected.")
        else:
            continue
    elif "Goodbye".lower() in user_input:
        break
    else:
        print(random.choice(words_list))

print("Goodbye, " + student_name + ".")