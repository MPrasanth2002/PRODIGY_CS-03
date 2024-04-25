import re

def password_complexity_checker(password):
    # Check length
    Length = len(password) >= 13

    # Check for uppercase letters
    Uppercase = bool(re.search(r'[A-Z]', password))

    # Check for lowercase letters
    Lowercase = bool(re.search(r'[a-z]', password))

    # Check for numbers
    Numbers = bool(re.search(r'[0-9]', password))

    # Check for special characters
    Special_character = bool(re.search(r'[!@#$%^&*(),-_+=;/\.?":{}|<>]', password))

    # Calculate total score
    Total_score = Length + Uppercase + Lowercase + Numbers + Special_character

    # Provide feedback based on total score
    if Total_score == 5:
        return "You Entered a Strong password"
    elif Total_score >= 3:
        return "You Entered a Good password"
    else:
        return "You Entered a Weak password"

password = input("Enter your password: ")
strength = password_complexity_checker(password)
print(f"Password strength: {strength}")
