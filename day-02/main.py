import secrets
import string
from getpass import getpass

DEFAULT_LENGTH = 16
MIN_LENGTH = 8
MAX_LENGTH = 128
MAX_SCORE = 6

COMMON_PASSWORDS = {
    "password", "12345", "12345678", "gabriel", "123456789", "11111", "123abc", "iloveyou", "admin", "welcome",    
}

def ask_length():
    answer = input(f"Password length: {MIN_LENGTH}--{MAX_LENGTH}, press enter for {DEFAULT_LENGTH}: \n").strip()
    if not answer:
        return DEFAULT_LENGTH

    try:
        length = int(answer)
    except ValueError:
        print("Please enter a number.")
        return None
    if length < MIN_LENGTH or length > MAX_LENGTH:
        print(f"Length must be between {MIN_LENGTH} and {MAX_LENGTH}")
        return None

    return length

def ask_yes_no(question):
    answer = input(f"{question} (y/n, press enter for yes): \n").strip().lower()
    return answer not in ("n", "no")


def generate_password(length, pools):
    password_chars = [secrets.choice(pool) for pool in pools]

    allcharacters = "".join(pools)
    remaining = length - len(password_chars)
    password_chars += [secrets.choice(allcharacters) for _ in range(remaining)]
   
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)

def check_strength(password):
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["This is one of the most common password. It would be guessed instantly."]

    score = 0
    feedback = []

    if len(password) >= 12:
        score +=1
    else:
        feedback.append("Use atleast 12 characters!")

    if len(password) >=16:
        score +=1

    if any(char.islower() for char in password):
        score +=1
    else:
        feedback.append("Add lowercase letters.")

    if any(char.isupper() for char in password):
        score +=1
    else:
        feedback.append("Add uppercase letters.")

    if any(char.isdigit	() for char in password):
        score +=1
    else:
        feedback.append("Add numbers.")

    if any(char in string.punctuation for char in password):
        score +=1
    else:
        feedback.append("Add symbols such as !, @, $.")

    return score, feedback

def strength_label(score):
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Fair"
    if score == 5:
        return "Good"
    return "Strong"


def generate_flow():
    length = ask_length()
    if length is None:
        return

    pools = []
    if ask_yes_no("Include lowercase letter?"):
        pools.append(string.ascii_lowercase)
    if ask_yes_no("Include uppercase letter?"):
        pools.append(string.ascii_uppercase)
    if ask_yes_no("Include numbers"):
        pools.append(string.digits)
    if ask_yes_no("Include symbols?"):
        pools.append(string.punctuation)
    
    if not pools:
        print("You need at least one character type:")
        return

    password = generate_password(length, pools)
    score, _ = check_strength(password)
    print(f"Your password is: {password}")
    print(f"Strength: Your password strength: {strength_label(score)}, ({score}/{MAX_SCORE})")

def check_flow():
    password = getpass("Please enter your password (typing is hidden):\n ")

    if not password:
        print("There is no password typed yet!")
        return

    score, feedback = check_strength(password)
    print(f"Strength: Your password strength: {strength_label()}, ({score}/{MAX_SCORE})")

    if feedback:
        print("How to improve it.")
    for tip in feedback:
        print(f"- {tip}")
    else:
        print("There is no issue found!")

def show_menu():
    print("\n=== Password Tool ===")
    print("1. Generate a password")
    print("2. Check a password")
    print("3. Quit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            generate_flow()
        elif choice == "2":
            check_flow()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please pick a number from 1 to 3.")

if __name__ == "__main__":
    main()
