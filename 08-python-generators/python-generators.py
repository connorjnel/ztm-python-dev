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

# class MyGen():
#     current = 0

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyGen.current < self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration


# gen = MyGen(0, 100)
# for i in gen:
#     print(i)

# Fibonacci sequence

def fib(number):
    a = 0
    b = 1
    for i in range(number + 1):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib(20):
    print(x)
