# My solution
# def highest_even(li):
#     '''Find highest even number in list, sort first in reverse then modulo'''
#     li.sort(reverse=True)
#     for item in li:
#         if item % 2 == 0:
#             return item

# Couse Solution
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11, 50]))
