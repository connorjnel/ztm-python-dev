from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(item):
    return item.capitalize()


mapped_list = list(map(capitalize, my_pets))

print(mapped_list)


# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

zipped_list = list(zip(my_strings, my_numbers[::-1]))  # Can also use sorted

print(zipped_list)


# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def score(item):
    return item > 50


filtered_list = list(filter(score, scores))

print(filtered_list)

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def total(acc, item):
    return acc + item


reduced_list1 = reduce(total, my_numbers, 0)
reduced_list2 = reduce(total, scores, 0)

# alternative solution
# print(reduce(accumulator, (my_numbers + scores))) -> Nice way to get around argument limits

final_list = reduced_list1 + reduced_list2

print(final_list)
