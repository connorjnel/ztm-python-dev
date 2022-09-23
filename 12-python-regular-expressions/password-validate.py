# at least 8 characters, max 15 characters
# contain any letters, numbers, $%#@
# at least one symbol, one number, one letter
# self made is at least 8 chracters, symbol and letter, defined symbols, ends with number

import re

regex = re.compile(
    r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d$%#@]{8,15}$")
self_made_regex = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")

user_password = "abcddsfsdfh523$"

password = regex.fullmatch(user_password)

if password:
    print("Password is acceptable")
else:
    print("password not accepted")
