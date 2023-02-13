# Class and Sub-Classes practice work


class User:

  def sign_in(self):
    print('logged in')


class Wizard(User):

  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with power of {self.power}')


class Archer(User):

  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows, arrows left: {self.num_arrows}')


wizard1 = Wizard('Merlin', 60)

print(wizard1.name)
print(wizard1.power)
print(wizard1.sign_in())
wizard1.attack()

archer1 = Archer('Robin', 25)

print(archer1.name)
print(archer1.num_arrows)
print(archer1.sign_in())
archer1.attack()