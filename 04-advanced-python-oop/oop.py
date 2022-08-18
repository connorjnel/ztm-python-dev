# class PlayerCharacter:
#     # Class object attribute
#     membership = True

#     def __init__(self, name="Anon", age=0):
#         if (age > 18):
#             self.name = name  # Attributes
#             self.age = age  # Attributes

#     def shout(self):
#         # print(f"My name is {self.name}")
#         return self

#     @classmethod
#     def adding_things(cls, num1, num2):
#         return num1 + num2

#     @staticmethod
#     def adding_things2(num1, num2):
#         return num1 + num2


# player1 = PlayerCharacter("Jovan", 24)
# player2 = PlayerCharacter("Tom", 50)
# player3 = PlayerCharacter("Nick", 10)

# print(player1.shout())

class User():
    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrow, arrows left: {self.num_arrows}")


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin Hood", 100)

# wizard1.attack()
# archer1.attack()

print(isinstance(wizard1, object))
