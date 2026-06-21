import random
import string

chars = string.punctuation + string.digits + string.ascii_letters

print("Welcome to the Password Generator!")
print("\nYour new passord is:")
print("--------------------------")
print(chars)
print("--------------------------")

#Making all the characters in this String into list elements.

char = string.punctuation + string.digits + string.ascii_letters + " "
char = list(char)
key = char.copy()

random.shuffle(key) #to make sure key and schar do not share the same characters i.e both key and char hve different characters.

#print(f"char: {char}")
#print(f"key : {key}")

#ENCRYPTION: To encrypt, we will replace every instance of one character within that string i.e. one character is replaced by another. Every time this program is run this key will be reshuffled.

plain_text = input("Enter a message to encrypt:")
cipher_text = ""

for letter in plain_text: #we are iterating over every character in the message typed by the user
    index =char.index(letter)
    cipher_text += key[index]

print(f"Original message: '{plain_text}'")
print(f"Encrypted message: '{cipher_text}'")

#DECRYPT
cipher_text = input("Enter a message to encrypt:")
plain_text = ""

for letter in cipher_text: #we are iterating over every character in the message typed by the user
    index =key.index(letter)
    plain_text += char[index]

print(f"Encrypted message: '{cipher_text}'")
print(f"Original message: '{plain_text}'")
