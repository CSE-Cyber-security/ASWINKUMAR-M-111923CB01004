#!/usr/bin/env python3
"""A simple password strength checker for educational use."""

import getpass
import string


def check_password(password: str) -> dict:
    """Return the result of each password-strength criterion."""
    return {
        "Length (at least 8 characters)": len(password) >= 8,
        "Uppercase letter (A-Z)": any(char in string.ascii_uppercase for char in password),
        "Lowercase letter (a-z)": any(char in string.ascii_lowercase for char in password),
        "Number (0-9)": any(char in string.digits for char in password),
        "Special symbol": any(char in string.punctuation for char in password),
    }


def get_strength(results: dict) -> str:
    """Determine strength based on the number of satisfied criteria."""
    score = sum(results.values())
    if score == 5:
        return "Strong"
    if score >= 3:
        return "Moderate"
    return "Weak"


def main() -> None:
    print("=" * 42)
    print("       PASSWORD STRENGTH CHECKER")
    print("=" * 42)
    # getpass avoids displaying the password while typing in a terminal.
    password = getpass.getpass("Enter a password to check: ")

    results = check_password(password)
    print("\nPassword Criteria:")
    for criterion, passed in results.items():
        print(f"{criterion}: {'Satisfied' if passed else 'Not Satisfied'}")

    print(f"\nPassword Strength: {get_strength(results)}")


if __name__ == "__main__":
    main()
