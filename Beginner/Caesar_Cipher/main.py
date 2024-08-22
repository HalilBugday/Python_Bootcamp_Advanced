from art import logo
from dec_enc import encrypt, decrypt

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def menu(choice):
    if choice == "encode":
        encrypt(orginal_text=text, shift_amount=shift) #keyword arg.
    elif choice == "decode":
        decrypt(text, shift) #positional arg.
    else:
        print("Invalid choice!")

menu(direction)  # Call the menu function with the user's choice.