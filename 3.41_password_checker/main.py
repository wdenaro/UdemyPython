#Password checker 3.41

username = input('Please enter your username: ')

password = input('Please enter your password: ')

obfuscated_password = '*' * len(password)

print(
  f'\nHello {username},\nyour password ({obfuscated_password}) is {len(obfuscated_password)} characters long.\n'
)