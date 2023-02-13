str = 'The qui-quux is the quux-quux.'

if len(str) > 10:
  print(f'String is too long, it is {len(str)} chars long.')

# Using walrus operator to assign a value that can be used in the
# conditional block

if (n := len(str)) > 10:
  print(f'String is too long, it is {n} chars long.')

while (n := len(str)) > 1:
  print(str)
  str = str[:-1]

print(str)