import random
import string
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        print("Error: Please select at least one character type.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the length of the password: "))
        use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            print("Your generated password is:", password)
        else:
            print("Password generation failed.")
    except ValueError:
        print("Error: Please enter a valid length.")
        
if __name__ == "__main__":
    main()
