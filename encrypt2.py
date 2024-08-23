from cryptography.fernet import Fernet
import random
import string

def encrypt_string(string, key):
    f = Fernet(key)
    encrypted_string = f.encrypt(string.encode())
    return encrypted_string

# Strings to encrypt and save
string1 = "Test"
string2 = "World"
codes = []
letters = []

# Encryption key
encryption_key = Fernet.generate_key()

for i in range(6):
    code = random.randint(1, 10)
    letter = random.choice(string.ascii_letters)
    codes.append(code)
    letters.append(letter)

print(encryption_key.decode('utf-8'))
print(codes[0], codes[1], codes[2])
print(letters[0], letters[1], letters[2])

key2 = encryption_key.decode('utf-8')

for i in range(6):
    new_key = key2[:codes[i]] + letters[i] + key2[codes[i]:]
    key2 = new_key

print(new_key)

# Encrypt the strings
encrypted_string1 = encrypt_string(string1, encryption_key)
encrypted_string2 = encrypt_string(string2, encryption_key)

# Save the encrypted strings and encryption key to the file
file_path = "test.txt"
with open(file_path, 'wb') as file:
    file.write(encrypted_string1 + b'\n')
    file.write(encrypted_string2 + b'\n')
    file.write(encryption_key)
