'''Dictionary'''

user = {
    "basket": [1, 2, 3],
    "greet": "Hello",
}

print(user.get("basket"))

user["basket"] = ["eggs", "milk", "bread"]

print(user.get("age", 50))

print(user.get("age"))


user2 = dict(name="John")

print(user)

print("age" in user.keys())

# print(user.clear())

user3 = user.copy()
print(user3)
user3["greet"] = "Goodbye"
print(user3)
