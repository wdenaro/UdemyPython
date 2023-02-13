# OOP Class practice

class PlayerCharacter:

    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name
            self.age = age

    def shout(self):
        print(f'MY NAME IS {self.name.upper()}!')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

player1.powers = ['Telepathic', 'Clairvoyant']

print(player1.powers)
print(player2.name)
print(player2.age)
print(player2.membership)
print(player2.shout())