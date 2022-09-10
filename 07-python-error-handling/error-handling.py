# print(1 + "True")  # Generates TypeError

# Error Handling

# while True:
#     try:
#         age = int(input("What is your age\n"))
#         10/age
#     except ValueError:
#         print("Please enter a number")
#     except ZeroDivisionError:
#         print("Please enter age higher than 0")
#     else:
#         print("thank you")
#         break

def sum(num1, num2):
    try:
        return num1 / num2
    # Can add multiple exceptions and save them as err variable and then print variable to show error
    except (TypeError, ZeroDivisionError) as err:
        print(err)


print(sum("1", 0))
