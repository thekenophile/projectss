#bibhuti koirala
#student id_2417754
def welcome():
    print("Welcome to the Caesar cipher")
    print("This program encrypts and decrypts text with Caesar Cipher,")
welcome()
#
def enter_message():
    while true:
        pop=input("press(e)to encrpt and(d) to decrpt:")
        if(pop.lower()=="e"or pop.lower()=="d"):
            break
    if(pop.lower =="e"):
            user=input("would you like to encrypt:")
            shift=int(input("enter a shift value:"))
    else:
                user=input("would you like to decrypt:")
                shift=int(input("enter a shift value:"))
                enter_message()
#
def encrypt(message,shift):
    encrypted_result=""
    for char in message:
        if char.isalpha():
            upper_char=char.upper()
            encrypted_result+=chr((ord(upper_char)+shift-65)%26+65)
        else:
            encrypted_result+=char
    return encrypted_result


def decrypt(message,shift):
    return encrypt(message,-shift)
#
import os

def process_file(filename, mode, shift):
    messages = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                messages.append(encrypt_decrypt(line.strip(), mode, shift))
    except FileNotFoundError:
        print("File not found.")
    return messages

def is_file(filename):
    return os.path.isfile(filename)

def write_messages(messages):
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')

def message_or_file():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        input_source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if input_source in ['f', 'c']:
            break
        else:
            print("Invalid Input Source")

    filename = None
    if input_source == 'f':
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")

    message = None
    if input_source == 'c':
        while True:
            message = input("What message would you like to {} : ".format("encrypt" if mode == 'e' else "decrypt")).upper()
            if message:
                break

    shift = None
    if mode == 'e':
        while True:
            try:
                shift = int(input("What is the shift number: "))
                break
            except ValueError:
                print("Invalid Shift")

    return mode, message, filename, shift

def encrypt_decrypt(message, mode, shift):
    result = ""
    for char in message:
        if char.isalpha():
            # Shift the character by the specified amount
            shifted_char = chr((ord(char) - ord('A' if char.isupper() else 'a') + shift) % 26 + ord('A' if char.isupper() else 'a'))
            result += shifted_char
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

    while True:
        mode, message, filename, shift = message_or_file()
        result = process_file(filename, mode, shift) if filename else [encrypt_decrypt(message, mode, shift)]

        for encrypted_message in result:
            print(encrypted_message)

        write_messages(result)

        another = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another != 'y':
            print("Thanks for using the program, goodbye!")
            break

if __name__ == "__main__":
    main()
