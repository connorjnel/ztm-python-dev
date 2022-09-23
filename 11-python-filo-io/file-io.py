# my_file = open("test.txt")

# print(my_file.read())
# my_file.close()

try:
    with open("app/sad.xt", mode="r") as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("File does not exist")
    raise err
