some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# Function solution

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# print(duplicates)


duplicates = [char for char in set(some_list) if some_list.count(char) > 1]

duplicates2 = [char for char in some_list if some_list.count(char) > 1]
duplicates3 = list(set(duplicates2))

print(duplicates3)
