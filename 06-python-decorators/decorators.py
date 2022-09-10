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


# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print("********")
#         func(*args, **kwargs)
#         print("********")
#     return wrap_func


# @my_decorator
# def hello(greeting, emoji):
#     print(greeting + emoji)


# hello("hi", "🦕")

# Performance operator
from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"it took {t2-t1} s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i * 5


long_time()
