COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]


def check_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters (12 or more is better).")

    # Character types
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Add symbols like ! @ # $.")

    # Common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a very common password. Avoid it.")

    return score, feedback


def get_rating(score):
    if score >= 6:
        return "Strong"
    elif score >= 4:
        return "Medium"
    return "Weak"


def main():
    password = input("Enter a password to check: ")
    score, feedback = check_password(password)

    print(f"\nStrength: {get_rating(score)} (score {score}/6)")
    for tip in feedback:
        print(f"- {tip}")


main()