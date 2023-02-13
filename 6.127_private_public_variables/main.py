class PlayerCharacter:

  def __init__(self, name, age):
    self._name = name
    self._age = age

  def run(self):
    print('run')

  def speak(self):
    print(f'My name is {self._name} and I am {self._age} years old.')


player1 = PlayerCharacter('Spanghew Jones', 43)

print(player1._name)
print(player1._age)
player1.run()
player1.speak()