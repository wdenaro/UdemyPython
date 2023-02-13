birth_year = input('What year were you born? ')

bday_yet = input('Has your birthday occured this year yet? [y/n] ')

if (bday_yet.lower() == 'y'):
  age = 2023 - int(birth_year)

else:
  age = 2022 - int(birth_year)

print(f'Your age is {age}.')