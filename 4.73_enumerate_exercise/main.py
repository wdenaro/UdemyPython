#Enumerate exercise

alphabet = list('abcdefghijklmnopqrstuvwxyz')

ordinals = ('1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th',
            '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th',
            '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th',
            '26th')

for i, letter in enumerate(alphabet):
  if (letter == 'w'):
    print(f'The index of {letter} is {i}')
    print('...making it the ' + ordinals[i] + ' letter of the alphabet.')