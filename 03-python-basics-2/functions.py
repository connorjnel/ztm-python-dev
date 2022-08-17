# Functions

# name = input("what is your name?")

# def say_hello():
#     print("hello " + name)

# say_hello()

# def say_hello2(name="test", emoji="😑"):
#     print(f"Hello {name} {emoji}")


# say_hello2("jovan", "🤓")
# say_hello2()

def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func


total = sum(10, 20)
print(total)

# total = sum(10, 5)
# print(sum(4, 5))
# print(total)
# print(sum(4, total))
