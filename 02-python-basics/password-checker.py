# Inputs for username and password
user_name = input("What is your Username?\n")
password = input("What is your Password?\n")

# Get password length and convert to masked string
password_length = len(password)
password_mask = password_length * "*"

print(f"{user_name}, your Password {password_mask} is {password_length} characters long")
