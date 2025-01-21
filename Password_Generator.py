# A program to generate random passwords.

import random
import string

def password_generator():
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated password: {password}")

password_generator()


'''
Explanation:
1. The user specifies the desired password length.
2. The program uses Python's random and string modules to select random characters (letters, digits, symbols).
3. It combines the characters into a string of the specified length.
'''
