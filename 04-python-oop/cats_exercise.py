# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat("Dark", 3)
cat2 = Cat("Anon", 5)
cat3 = Cat("Scooter", 8)

# 2 Create a function that finds the oldest cat

cats = [cat1.age, cat2.age, cat3.age]


def maxAge(list):
    oldest_cat = max(list)
    return oldest_cat


maxAge(cats)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {maxAge(cats)} years old")
