import random
import re
# Predefined list of weak passwords
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "qwerty", "abc123",
    "password1", "letmein", "12345678", "iloveyou"
]
# Function to check password strength


def check_password_strength(password):
    feedback = []
    score = 0
 # Check password length
    if len(password) < 8:
        feedback.append("Password is too short! Use at least 8 characters.")
    else:
        score += 1
 # Check for uppercase letters
    if not any(char.isupper() for char in password):
        feedback.append("Add at least one uppercase letter.")
    else:
        score += 1
 # Check for lowercase letters
    if not any(char.islower() for char in password):
        feedback.append("Add at least one lowercase letter.")
    else:
        score += 1
 # Check for digits
    if not any(char.isdigit() for char in password):
        feedback.append("Add at least one digit.")
    else:
        score += 1
 # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append(
            "Add at least one special character (!@#$%^&*(), etc.).")
    else:
        score += 1
 # Check against common passwords
    if password in COMMON_PASSWORDS:
        feedback.append(
            "Your password is too common. Choose a more unique one.")
    else:
        score += 1
 # Overall feedback
    if score < 3:
        feedback.insert(0, "Password is weak!")
    elif 3 <= score < 5:
        feedback.insert(0, "Password is moderate. Consider improving it.")
    else:
        feedback.insert(0, "Password is strong!")
    return feedback
# Function to generate a secure password


def generate_secure_password(length):
    if length < 8:
        return "Password length must be at least 8 characters."
 # Define character pools
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*(),.?\":{}|<>"
 # Ensure the password includes at least one of each type
    all_chars = lowercase + uppercase + digits + special
    password = random.choice(lowercase) + random.choice(uppercase) + \
        random.choice(digits) + random.choice(special)
 # Fill the rest of the password
    password += ''.join(random.choices(all_chars, k=length - 4))
 # Shuffle to avoid predictable patterns
    password = ''.join(random.sample(password, len(password)))

    return password
# Function to display program instructions


def display_instructions():
    return """
Welcome to the Password Management System!
1. Use 'Check Password Strength' to evaluate your password's security.
2. Use 'Generate a Secure Password' to create a strong, random password.
3. Ensure your passwords are at least 8 characters long, with a mix of letters,
digits, and special symbols.
"""
# Main menu system


def main_menu():
    while True:
        print("\n--- Password Management System ---")
        print("1. Check Password Strength")
        print("2. Generate a Secure Password")
        print("3. Program Instructions")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            password = input("Enter a password to check its strength: ")
            feedback = check_password_strength(password)
            print("\n".join(feedback))
        elif choice == "2":
            try:
                length = int(
                    input("Enter desired password length (minimum 8): "))
                password = generate_secure_password(length)
                print(f"Generated Password: {password}")
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == "3":
            print(display_instructions())
        elif choice == "4":
            print("Exiting the program. Stay safe!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


# Run the program
if __name__ == "__main__":
    main_menu()
