import secrets
import string

def generate_token(length):
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token

def main():
    try:
        num_tokens = int(input("How many tokens do you want to generate? "))
        for i in range(num_tokens):
            token = generate_token(4) + '.' + generate_token(64)
            print(token)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
