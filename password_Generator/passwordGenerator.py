import random
import string

def password_generator():
    characters = ""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    characters += lowercase
    characters += uppercase
    print("Generate a Password : \n")
    length = int(input("Enter the length of the password : "))
    digi = input("Do you want to include digits (y/n): ")
    symbs = input("Do you want to include symbols (y/n): ")
    if digi == "y" or digi == "Y":
        characters += digits
    if symbs == "y" or symbs == "Y":
        characters += symbols

    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("\nYour generated Password : ",password)

password_generator()