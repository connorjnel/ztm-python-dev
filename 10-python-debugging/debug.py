try:
    4 + "skjdnfknj"
except TypeError:
    print("Typerror happened, use strings")

list = [1, 2, 3, 4, 5]
list2 = ["John", "Mike", "Joe"]

for item in list:
    print(item * 5)

for name, item in list2, list:
    print(f"{name}, is a idiot and has a IQ of {item}")
