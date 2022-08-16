# Exercise - Check for duplicates in list

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# some_set = set(some_list)

# if (len(some_list)) == (len(some_set)):
#     print("No duplicates")
# else:
#     print("List has duplicates")

# dup = {x for x in some_list if some_list.count(x) > 1}
# print("Yes, duplicates exist and they are: " + str(dup))

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
