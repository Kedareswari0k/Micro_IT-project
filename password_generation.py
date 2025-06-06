import random
import string

def get_user_input():
    print("🔐 Password Generator - Secure & Customizable 🔐")

    # Get password length
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("❌ Password length must be at least 4.")
            else:
                break
        except ValueError:
            print("❌ Please enter a valid number.")

    # Get character type preferences
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    if not any([use_upper, use_lower, use_digits, use_special]):
        raise ValueError("⚠️ At least one character type must be selected.")

    while True:
        try:
            count = int(input("How many passwords do you want to generate? "))
            if count < 1:
                print("❌ Must generate at least one password.")
            else:
                break
        except ValueError:
            print("❌ Please enter a valid number.")

    return length, use_upper, use_lower, use_digits, use_special, count

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    character_pool = ''
    password = []

    if use_upper:
        character_pool += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if use_lower:
        character_pool += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if use_digits:
        character_pool += string.digits
        password.append(random.choice(string.digits))

    if use_special:
        character_pool += string.punctuation
        password.append(random.choice(string.punctuation))

    if len(password) > length:
        raise ValueError("Length too short for selected character types.")

    while len(password) < length:
        password.append(random.choice(character_pool))

    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length, use_upper, use_lower, use_digits, use_special, count = get_user_input()
        print("\n🔐 Generated Password(s):\n")
        for i in range(count):
            pwd = generate_password(length, use_upper, use_lower, use_digits, use_special)
            print(f"{i+1}. {pwd}")
    except ValueError as ve:
        print(f"\n❌ Error: {ve}")
    except Exception as e:
        print(f"\n⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    main()
