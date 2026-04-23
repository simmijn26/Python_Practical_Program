# Q16. Read file and count lines, words, characters

filename = input("Enter file name: ")

with open(filename, "r") as f:
    data = f.read()

lines = data.split("\n")
words = data.split()

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", len(data))