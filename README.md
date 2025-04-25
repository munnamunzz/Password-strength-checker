Shinchan Password Strength Checker

A Python-based password strength checker offering both a graphical user interface (GUI) and a command-line interface (CLI) to help users evaluate the robustness of their passwords.

Features
Dual Interface: Choose between a user-friendly GUI or a straightforward CLI.

Comprehensive Analysis: Evaluates passwords based on length, character variety, and inclusion of special characters.

Feedback Mechanism: Provides suggestions to enhance password strength.

Real-time Assessment: Instantly displays the strength level of the entered password.

Requirements
Python 3.x

Tkinter (usually included with standard Python installations)

Installation
Clone the Repository:

git clone https://github.com/munnamunzz/Password-strength-checker.git
cd shinchan-password-checker
Install Dependencies: Tkinter is typically included with Python. If not, install it using:

For Debian/Ubuntu:

sudo apt-get install python3-tk
For macOS (using Homebrew):

brew install python-tk
For Windows: Tkinter is usually included with Python. If not, consider reinstalling Python and ensuring Tkinter is selected during installation.

Usage
GUI Version
Launch the graphical interface:


python shinchan_gui.py
Enter your password in the input field.

Click the "Check Strength" button.

View the strength assessment and suggestions.

CLI Version
Run the command-line interface:


python shinchan.py
Follow the prompts to enter your password.

Receive immediate feedback on its strength and suggestions for improvement.
