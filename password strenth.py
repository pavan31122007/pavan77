import math
import re
import string


def calculate_entropy(password: str) -> float:
    """Calculates the Shannon entropy of a password to measure randomness."""
    if not password:
        return 0.0

    # Determine the pool size (L) based on character types present
    pool_size = 0
    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    # Shannon Entropy formula: H = Length * log2(Pool Size)
    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    return round(entropy, 2)


def check_password_strength(password: str) -> dict:
    """Evaluates password strength using rule-based criteria and entropy."""
    score = 0
    feedback = []

    # 1. Length Check
    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
        feedback.append("Increase length to 12+ characters for better safety.")
    else:
        feedback.append("Critical: Password is too short (under 8 characters).")

    # 2. Character Diversity Checks
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Missing lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Missing numerical digits.")

    if re.search(r"[" + re.escape(string.punctuation) + r"]", password):
        score += 1
    else:
        feedback.append("Missing special characters.")

    # 3. Calculate Entropy
    entropy_val = calculate_entropy(password)

    # 4. Final Rating Assignment
    if score >= 5 and entropy_val >= 60:
        rating = "Very Strong"
    elif score >= 4 and entropy_val >= 40:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return {
        "password": password,
        "score": f"{score}/6",
        "entropy": f"{entropy_val} bits",
        "rating": rating,
        "feedback": feedback if feedback else ["Password meets all criteria!"],
    }


# Example execution
if __name__ == "__main__":
    test_pwd = input("Enter a password to test: ").strip()
    result = check_password_strength(test_pwd)

    print("\n--- Cybersecurity Password Analysis ---")
    print(f"Rating:   {result['rating']}")
    print(f"Score:    {result['score']}")
    print(f"Entropy:  {result['entropy']}")
    print("\nFeedback:")
    for line in result["feedback"]:
        print(f"- {line}")