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
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))