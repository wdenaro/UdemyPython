#Iterable examples

#My dictionary
user = {
  'name': 'John',
  'age': 35,
  'address': '123 Main Street',
  'phone': '123-456-7890'
}

#Returns keys only
for item in user:
  print(item)

#Explicitly returns keys only
for item in user.keys():
  print(item)

#Returns values only
for item in user.values():
  print(item)

#Returns key|value pairs as a tuple
for item in user.items():
  print(item)

#Creates vars for the keys and values
for key, value in user.items():
  print(f'Key: {key} | Value: {value}')


#My cheat will multiply a string by an int to allow
#faux iteratation of an integer
for item in '.' * 10:
  print(item)


# ERROR Cannot iterate through a non iterable
for item in 10:
  print(item)