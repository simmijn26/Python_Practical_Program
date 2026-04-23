# Q17. Copy contents of one file to another after removing digits

src = input("Enter source file name: ")
dest = input("Enter destination file name: ")

with open(src, "r") as f:
    data = f.read()

new_data = ""

for ch in data:
    if not ch.isdigit():
        new_data += ch

with open(dest, "w") as f:
    f.write(new_data)

print("File copied after removing digits.")