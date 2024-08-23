from cryptography.fernet import Fernet

def encrypt_string(string, key):
    f = Fernet(key)
    encrypted_string = f.encrypt(string.encode())
    return encrypted_string

# Strings to encrypt and save
string1 = "Test"
string2 = "World"

# Encryption key
encryption_key = Fernet.generate_key()

# Encrypt the strings
encrypted_string1 = encrypt_string(string1, encryption_key)
encrypted_string2 = encrypt_string(string2, encryption_key)

# Save the encrypted strings and encryption key to the file
file_path = "test.txt"
with open(file_path, 'wb') as file:
    file.write(encrypted_string1 + b'\n')
    file.write(encrypted_string2 + b'\n')
    file.write(encryption_key)
