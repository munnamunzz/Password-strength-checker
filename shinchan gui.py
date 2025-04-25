import tkinter as tk
from tkinter import messagebox
import re

def check_strength():
    password = entry.get()
    score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 10:
        score += 1
    else:
        feedback.append("Password should be at least 10 characters long.")

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

    result_label.config(text=f"Password Strength: {strength_levels[score]}")
    feedback_text.delete("1.0", tk.END)
    if feedback:
        feedback_text.insert(tk.END, "Suggestions:\n")
        for f in feedback:
            feedback_text.insert(tk.END, f"- {f}\n")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

# Entry widget
entry_label = tk.Label(root, text="Enter Password:")
entry_label.pack(pady=10)
entry = tk.Entry(root, width=30, show="*")
entry.pack()

# Check button
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Password Strength: ")
result_label.pack(pady=10)

# Feedback text
feedback_text = tk.Text(root, height=5, width=50)
feedback_text.pack(pady=10)

root.mainloop()
