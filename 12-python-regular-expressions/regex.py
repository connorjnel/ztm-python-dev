import re

pattern = re.compile(r"([a-zA-Z]).([a])")
string = "Search inside of this text please!"

# Simple way to search for text inside string, returns bool
# print("Search" in string)

# Using py re, returns object with location or None if not found
a = re.search("thiste", string)

# Using pattern to search
b = pattern.search(string)
print(b)
