class PlayerCharacter:
    # Class object attribute
    membership = True

    def __init__(self, name="Anon", age=0):
        if (age > 18):
            self.name = name  # Attributes
            self.age = age  # Attributes

    def shout(self):
        # print(f"My name is {self.name}")
        return self

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Jovan", 24)
player2 = PlayerCharacter("Tom", 50)
player3 = PlayerCharacter("Nick", 10)

print(player1.shout())
