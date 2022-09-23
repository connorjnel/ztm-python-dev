import re

email_regex = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "b@b.com"

# Simple way to search for text inside string, returns bool
# print("Search" in string)

# Using py re, returns object with location or None if not found
a = re.search("thiste", string)

# Using pattern to search
b = email_regex.search(string)
print(b)

if b:
    print("email accepted")
else:
    print("fix your email input")
