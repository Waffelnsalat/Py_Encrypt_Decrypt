from cryptography.fernet import Fernet

file_path = "test.txt"

file = open(file_path, 'rb')

lines = file.readlines()

file.close()

key = lines[-1].strip()
string1 = lines[0]
string2 = lines[1]

f = Fernet(key)

de1 = f.decrypt(string1).decode('utf-8')
de2 = f.decrypt(string2).decode('utf-8')

print(de1)
print(de2)
