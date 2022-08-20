# Set and Dictionary Comprehensions

# Set comprehension method

my_set2 = {char for char in "hello"}

print(my_set2)

# Dict comprehension method

simple_dict = {
    "a": 1,
    "b": 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}

print(my_dict)
