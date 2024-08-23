file_path = "test.txt"
file = open(file_path, "r")

lines = file.readlines()

file.close()


line_number = 1

wline = lines[line_number]

print(wline)