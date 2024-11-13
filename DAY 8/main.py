from encode_decode import encode, decode
from caesar_cipher_art import art
import os
os.system('cls')
status = "yes"
print(art)
while status == "yes":    
    start = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
    message = input("Type  your message:\n")
    shift = input("Type the shift number:\n")
    if start == 'encode':
        print(f"Your encoded message is:\n{encode(message, shift)}")
    if start == 'decode':
        print(f"Your decoded message is:\n{decode(message, shift)}")
    status = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    os.system('cls')
