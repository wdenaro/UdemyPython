class Player:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(Player):

    def __init__(self, name, email, power):
        super().__init__(name, email)
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(Player):

    def __init__(self, name, email, num_arrows):
        super().__init__(name, email)
        self.num_arrows = num_arrows

    def attack(self):
        if self.num_arrows > 0:
            self.num_arrows -= 1
            print(f'attacking with arrows, arrows left: {self.num_arrows}')
        else:
            print(f'you are out of arrows! Oh Nooooooo!!!!!')


wizard1 = Wizard('Merlin', 'merlin@gmail.com', 60)
print(wizard1.name)
print(wizard1.email)
print(wizard1.power)
wizard1.sign_in()
wizard1.attack()

archer1 = Archer('Robin', 'r.hood@castle.net', 25)
print(archer1.name)
print(archer1.email)
print(archer1.num_arrows)
archer1.sign_in()
archer1.attack()