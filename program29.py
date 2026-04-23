# Q29. Regex validate email and phone

import re

email = input("Enter email: ")
phone = input("Enter phone: ")

if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.fullmatch(r"\d{10}", phone):
    print("Valid Phone")
else:
    print("Invalid Phone")