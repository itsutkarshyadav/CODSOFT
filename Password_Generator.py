import random

def generate_password(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*-+1234567890"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

while True:
    user_input = input("Enter password length (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    elif user_input.isdigit():
        length = int(user_input)
        if length > 0:
            print("Your password is:", generate_password(length))
        else:
            print("Password length must be greater than 0.")
    else:
        print("Invalid input. Please enter a valid number.")