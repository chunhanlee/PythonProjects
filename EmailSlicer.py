try:
    email = input("Please enter a valid email: ").strip()
    if '@' not in email:
        raise Exception("That is not a valid email format")
except:
    print("That is not a valid email format")
else:
    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]
    print(f"Your username is {username} and your domain is {domain}")