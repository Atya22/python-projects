#!/usr/bin/python3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

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
    

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "decode":
    decrypt(text, shift)
elif direction == "encode":
    encrypt(text, shift)