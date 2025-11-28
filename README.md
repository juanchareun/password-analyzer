# 🔒 Password Strength Analyzer (Python)

[![Project Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()
[![Language](https://img.shields.io/badge/Language-Python%203.x-blue)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

## 💡 Project Overview

This is a Python-based **Command-Line Interface (CLI)** tool designed to evaluate the security and robustness of user-provided passwords. It goes beyond simple length checks by calculating a numerical score based on complexity and performing critical checks against a small list of common/breached passwords.

Built as a fundamental demonstration of secure coding principles, this tool simulates the logic used in modern authentication systems to enforce strong password policies.

## 🧠 Security Methodology & Key Features

The analyzer provides detailed, actionable feedback based on a multi-factor scoring system:

* **Complexity Scoring:** Uses **regular expressions** to award points for the presence of four key character types: Uppercase, Lowercase, Digits, and Special Characters.
* **Blacklist Integration:** Checks the input password against an integrated list of common and known compromised passwords. **Any password found on this list is immediately flagged as 'Very Weak' regardless of its complexity.**
* **Actionable Feedback:** Provides specific recommendations on how to increase the password's security score (e.g., "Add a special character," "Increase length beyond 12 characters").
* **Minimal Requirements:** Runs with only standard Python libraries (`re`).

---

## 💻 Demonstration

To quickly understand the project's functionality, observe the following terminal outputs.

### Weak Password Example

Shows how the blacklist overrides complexity and provides critical warnings.



### Strong Password Example

Shows a high score and "Strong" rating based on variety and length.



---

## 🚀 Installation & Usage

### Prerequisites

* **Python 3.8+** (Required)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/juanchareun/password-analyzer.git
    ```
2.  **Navigate to the script directory:**
    ```bash
    cd password-analyzer
    ```

### How to Run

Execute the script directly from your terminal:

```bash
python password_analyzer.py

