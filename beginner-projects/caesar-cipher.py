#!/usr/bin/python3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift_amount, direction):
    new_text = ""
    index = len(alphabet) - shift_amount
    for i in text:
        index_element = alphabet.index(i)
        if direction == "decode":
            if index_element < index:
                new_text += alphabet[index_element - shift_amount]
            else:
                new_text += alphabet[index_element + len(alphabet) - shift_amount]
        elif direction == "encode":
            if index_element < index:
                new_text += alphabet[index_element + shift_amount]
            else:
                new_text += alphabet[index_element - len(alphabet) + shift_amount]
    print(f"The decrypted text is {new_text}")