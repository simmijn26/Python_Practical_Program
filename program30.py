# Q30. Regex password strength

import re

pwd = input("Enter password: ")

if (len(pwd) >= 8 and
    re.search(r"[A-Z]", pwd) and
    re.search(r"[a-z]", pwd) and
    re.search(r"\d", pwd) and
    re.search(r"[@$!%*?&]", pwd)):
    print("Strong Password")
else:
    print("Weak Password")