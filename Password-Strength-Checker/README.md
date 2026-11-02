# Password Strength Checker

A beginner-friendly Python command-line application that checks a password against five basic security criteria.

## Features

- Checks whether the password has at least 8 characters.
- Checks for at least one uppercase letter (`A-Z`).
- Checks for at least one lowercase letter (`a-z`).
- Checks for at least one digit (`0-9`).
- Checks for at least one special symbol (for example, `@`, `#`, `$`, `!`).
- Displays each criterion as **Satisfied** or **Not Satisfied**.
- Displays an overall strength rating: **Strong**, **Moderate**, or **Weak**.
- Uses `getpass` so the password is not shown while typing in a terminal.

## Requirements

- Python 3.8 or later
- No third-party packages required

## How to Run

1. Download or clone this repository.
2. Open a terminal or command prompt in the project folder.
3. Run:

   ```bash
   python password_checker.py
   ```

   On some systems, use `python3 password_checker.py`.

4. Enter a test password when prompted. The terminal hides the characters as you type.

## Example

For the sample password `Hello@123`, the program reports:

```text
==========================================
       PASSWORD STRENGTH CHECKER
==========================================
Enter a password to check:

Password Criteria:
Length (at least 8 characters): Satisfied
Uppercase letter (A-Z): Satisfied
Lowercase letter (a-z): Satisfied
Number (0-9): Satisfied
Special symbol: Satisfied

Password Strength: Strong
```

The password is hidden during actual input, so the example does not display it after the prompt.

## Strength Rules

- **Strong:** All 5 criteria are satisfied.
- **Moderate:** 3 or 4 criteria are satisfied.
- **Weak:** 0, 1, or 2 criteria are satisfied.

## Project Files

```text
Password-Strength-Checker/
├── password_checker.py
├── README.md
└── screenshots/
    └── output.png
```

## Screenshot

Add a screenshot of the program running in your terminal to the `screenshots/` folder and name it `output.png`. See the submission notes if your environment does not allow capturing a terminal screenshot directly.

## Learning Outcomes

- Python strings and character checks
- Conditional statements and functions
- Iterating over dictionary items
- Basic password security concepts
- GitHub repository and version-control workflow

## Disclaimer

This is a basic educational checker, not a complete password-security assessment. It does not detect common passwords, breached passwords, or predictable patterns. Do not enter a real or reused password into a demonstration application.
