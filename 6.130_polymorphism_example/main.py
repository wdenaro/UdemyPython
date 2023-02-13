# Polymorphism


class User:

  def sign_in(self):
    print('logged in')

  def attack(self):
    print('do nothing')


class Wizard(User):

  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    User.attack(self)
    print(f'attacking with power of {self.power}')


class Archer(User):

  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    if self.num_arrows > 0:
      print(f'attacking with arrows, arrows left: {self.num_arrows}')
      self.num_arrows -= 1
    else:
      print(f'you are out of arrows! Oh Nooooooo!!!!!')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 1)


def player_attack(character):
  character.attack()


player_attack(wizard1)
player_attack(archer1)

for character in [wizard1, archer1]:
  character.attack()