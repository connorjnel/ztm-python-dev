# def hello():
#     print("helloooo")


# greet = hello

# print(greet())

# del hello

# def greet(func):
#     func()


# def greet2():
#     def func():
#         return 5
#     return func


def my_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("********")
    return wrap_func


@my_decorator
def hello():
    print("hello")


@my_decorator
def bye():
    print("See you later")


hello()
