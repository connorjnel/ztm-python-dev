from audioop import reverse


def highest_even(li):
    li.sort(reverse=True)
    for item in li:
        if item % 2 == 0:
            return item


print(highest_even([10, 2, 3, 4, 8, 11, 50]))
