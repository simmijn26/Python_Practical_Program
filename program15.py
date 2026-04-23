# Q15. Count frequency of each word using dictionary

text = input("Enter a sentence: ").lower()

words = text.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequencies:")

for word in freq:
    print(word, ":", freq[word])