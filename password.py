# import random
# # import secrets
# import string
# from argparse import ArgumentParser



# def generator(min_length, numbers=True, special_characters=True):


#     letters = string.ascii_letters
#     digits = string.digits
#     special = string.punctuation

#     chars = letters
#     if numbers:
#         chars += digits
#     if special_characters:
#         chars += special

#     password = ""
#     meets_criteria = False
#     has_number = False
#     has_special = False

#     while not meets_criteria or len(password) < min_length:
#         new_char = random.choice(chars)
#         password += new_char

#         if new_char in digits:
#             has_number = True
#         elif new_char in special:
#             has_special = True

#         meets_criteria = True
#         if numbers:
#             meets_criteria = has_number
#         if special_characters:
#             meets_criteria = meets_criteria and has_special

#     return password

#     # print(letters, digits, characters)

# # min_length = int(input("Enter the minimum length: "))

# has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
# has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

# password = generator(8, has_number, has_special)
# print("The generated password is:", password)



import random
import string
from argparse import ArgumentParser

def generate_password(min_length=8, include_numbers=True, include_special_chars=True):
    """
    Generate a random password with a minimum length and optional inclusion of numbers and special characters.
    
    Args:
        min_length (int, optional): Minimum length of the password. Default is 8.
        include_numbers (bool, optional): Include numbers in the password. Default is True.
        include_special_chars (bool, optional): Include special characters in the password. Default is True.
    
    Returns:
        str: The generated password.
    """
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(min_length))
    
    # Ensure the password meets the required criteria
    while not (any(char.isdigit() for char in password) or not include_numbers) or \
          not (any(char in string.punctuation for char in password) or not include_special_chars):
        password = ''.join(random.choice(characters) for _ in range(min_length))
    
    return password

if __name__ == "__main__":
    parser = ArgumentParser(description="Generate a random password")
    parser.add_argument("-l", "--length", type=int, default=8, help="Minimum length of the password")
    parser.add_argument("-n", "--no-numbers", action="store_false", dest="include_numbers", help="Exclude numbers from the password")
    parser.add_argument("-s", "--no-special-chars", action="store_false", dest="include_special_chars", help="Exclude special characters from the password")
    args = parser.parse_args()
    
    password = generate_password(args.length, args.include_numbers, args.include_special_chars)
    print(f"The generated password is: {password}")

