# def hello():
#     print("helloooo")


# greet = hello

# print(greet())

# del hello

def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func
