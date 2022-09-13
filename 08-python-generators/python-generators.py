# range(100)
# list(range(100))


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result


# my_list = make_list(100)
# print(my_list)

# def generator_function(num):
#     for i in range(num):
#         yield i*2


# g = generator_function(100)
# next(g)
# next(g)
# print(next(g))

# def gen_fun(num):
#     for i in range(num):
#         yield i


# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator)*2)
#         except StopIteration:
#             break


# special_for([1, 2, 3])

class MyGen():
    def __init__(self, first, last):
        self.first = first
        self.last = last


gen = MyGen(0, 100)
for i in gen:
    print(i)
