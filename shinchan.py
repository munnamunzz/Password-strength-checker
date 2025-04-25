import re

def check_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 10:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Strength level
    strength_levels = {
        5: "Very Strong 💪",
        4: "Strong 👍",
        3: "Moderate ⚠️",
        2: "Weak 👎",
        1: "Very Weak ❌",
        0: "Extremely Weak ❌"
    }

    print(f"\nPassword Strength: {strength_levels[score]}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    pwd = input("Enter a password to check its strength: ")
    check_strength(pwd)
