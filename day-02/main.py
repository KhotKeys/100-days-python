import secrets
import string

def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))

def main():
    password = generate_password()
    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()