# some_value = 8
# some_value *= 5

# print(some_value) 

# str1 = "This is a string"
# str2 = 'So is this'

# print(str2)

# long_string = '''
# kjndfsg
# lkmsdfng;lksdf
# lkmsdfnglk;sdmnfg
# lkmdfmngsodioijnsdaofkmlkj;ndfsg
# '''

# print(long_string)

# first_name = "jovan"
# last_name = "nel"
# full_name = first_name +  last_name

# print(full_name)

# print(type(int(str(100))))

# weather = "It\"s \nsunny"

# print(weather)

name = "Johnny"
age = 55

print(f"hi {name}. You are {age} years old") # Python 3 method for formatting string
print("hi {}. You are {} years old".format("Johhny", "55")) # Python 2 method with .format
print("hi {1}. You are {0} years old".format("Johhny", "55")) # changing order with index values
print("hi {new_name}. You are {age} years old".format(new_name = "Sally", age=100)) # using new variables