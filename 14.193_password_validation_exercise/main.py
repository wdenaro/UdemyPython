# Password validation
# Accept a password that is 8 or more characters long, may contain letters, numbers and the following
# special characters: $, %, #, @

import re

pattern = re.compile(r"^[a-zA-Z0-9$%#@]{7,}\d$")

while True:
    password = input('Please enter your password: ')

    if pattern.match(password):
        break
    else:
        print('\033[91m' + '\nPlease match the password criteria.' + '\033[0m')

print('\033[95m' + '\nPassword acceptable.' + '\033[0m')
