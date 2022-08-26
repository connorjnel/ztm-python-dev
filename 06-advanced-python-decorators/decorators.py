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
    def wrap_func(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("********")
    return wrap_func


@my_decorator
def hello(greeting, emoji):
    print(greeting + emoji)


hello("hi", "🦕")
