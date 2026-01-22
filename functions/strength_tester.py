def check_strength(password):
    score = 0
    reason = []

    if len(password) > 8 :
        score += 20
        reason.append("✓ Length 8+")
    else:
        reason.append("✗ Too short")
    if any(char.isdigit() for char in password):
        score += 20
        reason.append("✓ has digits")
    else: 
        reason.append("✗ has no digits")
    if any(char.isalpha() for char in password):
        score += 20
        reason.append("✓ has lettres")

    else:
        reason.append("✗ has no lettres")
    if any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password):
        score += 20
        reason.append("✓ Has symbols")

    else:
        reason.append("✗ No symbols")
    if len(password) > 12:
        score += 20
        reason.append("✓ very long!")
    return score , reason

def check():
    try:
        while True:
            password= input ("Enter a password to test (or 'q' to exit):")
            if password.lower() == 'q':
                break
            score , reasons = check_strength(password)
            for reason in reasons :
                print (reason)
            print()
            print(f"Your password strength score is {score}%\n")
    except KeyboardInterrupt:
        print("\n")
        print("goodbye see ya later !")


check()