# Pure function, no side effects generated
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


# print(multiply_by2([1, 2, 3]))

# Pure object - doesnt use class

wizard = {
    "name": "Merlin",
    "power": 50
}

# print(wizard["power"])

# Map function


def multiply_by4(item):
    return item*4


new_list = [1, 2, 3, 4, 5]

mapped_list = list(map(multiply_by4, new_list))


# Filter function


def only_odd(item):
    return item % 2 != 0


filtered_list = list(filter(only_odd, new_list))


# Zip Function

list_1 = [1, 2, 3, 4, 5]
list_2 = [10, 20, 30, 40, 50]

zipped_list = list(zip(list_1, list_2))

print(zipped_list)
