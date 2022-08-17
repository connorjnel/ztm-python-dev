# Functions

# name = input("what is your name?")

# def say_hello():
#     print("hello " + name)

# say_hello()

# def say_hello2(name="test", emoji="😑"):
#     print(f"Hello {name} {emoji}")


# say_hello2("jovan", "🤓")
# say_hello2()

# def sum(num1, num2):
#     def another_func(num3, num4):
#         return num3 + num4
#     return another_func(num1, num2)


# total = sum(10, 20)
# print(total)

# txt = ["haha", "lol"]


# total = sum(10, 5)
# print(sum(4, 5))
# print(total)
# print(sum(4, total))

# def test(a):
#     '''Info: This is a completely useless function, testing docstrings'''
#     print(a)


# help(test)


# def is_even(num):
#     return num % 2 == 0


# print(is_even(50))

def super_func(*args, **kwargs):
    total = 0
    print(args)
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))
