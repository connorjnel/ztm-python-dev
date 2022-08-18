class PlayerCharacter:
    # Class object attribute
    membership = True

    def __init__(self, name="Anon", age=0):
        if (age > 18):
            self.name = name  # Attributes
            self.age = age  # Attributes

    def shout(self):
        print(f"My name is {self.name}")


player1 = PlayerCharacter("Jovan", 24)
player2 = PlayerCharacter("Tom", 50)
player3 = PlayerCharacter("Nick", 10)

print(player3.shout())
