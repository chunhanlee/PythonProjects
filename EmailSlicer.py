try:
    email = input("Please enter a valid email: ").strip()
    if '@' not in email:
        raise Exception("That is not a valid email format")
    if '.' not in email[email.index('@') + 1:]:
        raise Exception("This is not a valid domain")
except Exception as e:
    print(e)
else:
    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]
    print(f"Your username is {username} and your domain is {domain}")