


incorrect_passwords_count = 0
with open('passwords.txt', 'r') as file:
    passwords = file.read().splitlines()


for password in passwords:
    if not (password[0].isupper() and any(char.isdigit() for char in password)):
        print(f"Incorrect Password: {password}")
        incorrect_passwords_count += 1
        
    
print(f"Total Incorrect Passwords: {incorrect_passwords_count}")




# def is_valid_password(password):
#     if password[0].isupper():
#         for char in password:
#             if char.isdigit():
#                 return True
            

# def check_passwords(file_path):
#     incorrect_passwords = 0

#     with open(file_path, 'r') as file:
#         passwords = file.readlines()

#         for password in passwords:
#             password = password.strip()

#             if not is_valid_password(password):
#                 print("Invalid password:", password)
#                 incorrect_passwords +=1

#     print("\nTotal number of incorrect passwords:", incorrect_passwords)

# file_path = "passwords.txt"