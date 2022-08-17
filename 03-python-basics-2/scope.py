# def test_lol():
#     name = "Jovan"
#     return name


# print(name)

# Exercise

# a = 1


# def confusion():
#     a = 5
#     return a


# print(a)
# print(confusion())

# total = 0


# def count(total):
#     total += 1
#     return total


# print(count(count(count(total))))

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)


outer()
