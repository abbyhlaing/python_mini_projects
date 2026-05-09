# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
#             "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
#             "u", "v", "w", "x", "y", "z"]

# # Accept input of a plaintext message
# plaintext = input("Enter the plaintext message: ")

# # Accept input of the key (positive integer between 1 and 25)
# while True:
#     try:
#         key = int(input("Enter the key (a positive integer between 1 and 25): "))
#         if 1 <= key <= 25:
#             break
#         else:
#             print("Invalid key. Please enter a positive integer between 1 and 25.")
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")

# # Encrypt the plaintext using the Caesar cipher
# ciphertext = ""

# for char in plaintext:
#     if char.isalpha():
#         # Determine whether the character is uppercase or lowercase
#         is_upper = char.isupper()
#         # Find the index of the character in the alphabet
#         char_index = alphabet.index(char.lower())
#         # Apply the Caesar cipher shift
#         shifted_index = (char_index + key) % 26
#         # Convert the shifted index back to a character
#         shifted_char = alphabet[shifted_index]
#         # Preserve the case of the original character
#         shifted_char = shifted_char.upper() if is_upper else shifted_char
#         # Append the shifted character to the ciphertext
#         ciphertext += shifted_char
#     else:
#         # If the character is not a letter, leave it unchanged
#         ciphertext += char

# # Display the ciphertext
# print("Ciphertext:", ciphertext)




alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]

plaintext = input("Enter the plaintext message: ")

while True:
    try:
        key = int(input("Enter the key (a positive integer between 1 and 25): "))
        if 1 <= key <= 25:
            break
        else:
            print("Invalid key. Please enter a positive integer between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

ciphertext = ''.join([alphabet[(alphabet.index(char.lower()) + key) % 26].upper() if char.isalpha() else char for char in plaintext])

print("Ciphertext:", ciphertext)