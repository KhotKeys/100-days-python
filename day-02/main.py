import secrets
import string

DEFAULT_LENGTH = 16
MIN_LENGTH = 8
MAX_LENGTH = 128

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

def main():
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
    print(f"Your password is: {password}")

if __name__ == "__main__":
    main()
