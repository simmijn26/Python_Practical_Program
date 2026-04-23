# Q8. Palindrome check (with and without slicing)

s = input("Enter a string: ")

# With slicing
if s == s[::-1]:
    print("Palindrome using slicing")
else:
    print("Not palindrome using slicing")

# Without slicing
rev = ""
for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome without slicing")
else:
    print("Not palindrome without slicing")