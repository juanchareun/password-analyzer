import re
from typing import List, Tuple

# --- Configuration ---
MIN_LENGTH = 12  # Minimum recommended length for a strong password
MIN_SCORE = 100  # Target score for a password to be considered "Strong"

# NOTE: In a real-world scenario, you would load a much larger list from a file (like a subset of rockyou.txt).
# For simplicity and speed, we use a small, representative list here.
WEAK_PASSWORDS = [
    "password", "123456", "qwerty", "admin", "secret", "portfolio", "juan123", "chareun"
]

def analyze_password_strength(password: str) -> Tuple[int, List[str], str]:
    """
    Analyzes password strength based on length, complexity, and blacklist check.

    Returns: A tuple containing (score, feedback_list, strength_rating).
    """
    score = 0
    feedback = []

    # 1. --- Length Check (Base Score) ---
    if len(password) >= MIN_LENGTH:
        score += 30
    elif len(password) >= 8:
        score += 15
        feedback.append(f"Weak: Increase length beyond {len(password)} characters.")
    else:
        feedback.append("Critical: Password is too short (less than 8 characters).")

    # 2. --- Complexity Checks (Add points for variety) ---
    
    # Uppercase letters (A-Z)
    if re.search(r"[A-Z]", password):
        score += 20
    else:
        feedback.append("Weak: Add uppercase letters (A-Z).")

    # Lowercase letters (a-z)
    if re.search(r"[a-z]", password):
        score += 20
    else:
        feedback.append("Weak: Add lowercase letters (a-z).")

    # Numbers (0-9)
    if re.search(r"\d", password):
        score += 20
    else:
        feedback.append("Weak: Add numbers (0-9).")

    # Special characters (!@#$%^&*)
    if re.search(r"[!@#$%^&*()_+=\-{}[\]|\\:;\"'<>,.?/`~]", password):
        score += 20
    else:
        feedback.append("Weak: Add special characters (e.g., !, @, #).")

    # 3. --- Blacklist Check (Override Score) ---
    if password.lower() in [wp.lower() for wp in WEAK_PASSWORDS]:
        score = 0  # CRITICAL failure
        feedback = ["CRITICAL: Password is on the common/breached password list!"]
        strength_rating = "Very Weak"
        return score, feedback, strength_rating

    # 4. --- Determine Final Rating ---
    if score >= MIN_SCORE:
        strength_rating = "Strong"
    elif score >= 70:
        strength_rating = "Good"
    elif score >= 40:
        strength_rating = "Moderate"
    else:
        strength_rating = "Weak"

    return score, feedback, strength_rating

def main():
    """Main function to run the password analyzer loop."""
    print("--- Password Strength Analyzer ---")
    print(f"Goal: Achieve a score of {MIN_SCORE} for a 'Strong' rating.")
    print("-" * 35)

    while True:
        password = input("Enter a password to analyze (or type 'exit'): ").strip()
        
        if password.lower() == 'exit':
            break

        if not password:
            continue

        score, feedback, rating = analyze_password_strength(password)

        print("\n[ Analysis Result ]")
        print(f"SCORE: {score}")
        print(f"RATING: {rating}\n")
        
        if rating in ["Strong", "Good"]:
            print("Status: 💪 Your password is reasonably secure.")
        else:
            print("Status: ⚠️ Needs improvement. Recommendations:")
            for item in feedback:
                print(f"  - {item}")
        print("-" * 35)

if __name__ == "__main__":
    main()