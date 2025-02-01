import re


def check_password_strength(password):
    # Define criteria
    length_criteria      = len(password) >= 8
    lowercase_criteria   = re.search (r'[a - z]', password) is not None
    uppercase_criteria   = re.search (r'[A - Z]', password) is not None
    digit_criteria       = re.search (r'[0 - 9]', password) is not None
    special_char_criteria = re.search (r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate score
    score = sum([
        length_criteria,
        lowercase_criteria,
        uppercase_criteria,
        digit_criteria,
        special_char_criteria
        ])

    # Evaluate password strength
    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Moderate"
    else:
        return "Weak"

# Get user input
password = input("Enter your password: ")

# Check and display password strength
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
