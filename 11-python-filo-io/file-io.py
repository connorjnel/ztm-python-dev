# my_file = open("test.txt")

# print(my_file.read())
# my_file.close()

with open("app/sad.txt", mode="r") as my_file:
    print(my_file.read())
