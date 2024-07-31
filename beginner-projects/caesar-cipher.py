#!/usr/bin/python3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    max_index = len(alphabet) - shift_amount
    for i in plain_text:
        index_element = alphabet.index(i)
        if index_element < max_index:
            cipher_text += alphabet[index_element + shift_amount]
        else:
            cipher_text += alphabet[index_element - len(alphabet) + shift_amount]

def decrypt(cipher_text, shift_amount):
    decrypt_text = ""
    min_index = len(alphabet) - shift_amount
    for i in cipher_text:
        index_element = alphabet.index(i)
        if index_element < min_index:
            decrypt_text += alphabet[index_element - shift_amount]
        else:
            decrypt_text += alphabet[index_element + len(alphabet) - shift_amount]
    print(f"The decrypted text is {decrypt_text}")

if direction == "decode":
    decrypt(text, shift)
elif direction == "encode":
    encrypt(text, shift)