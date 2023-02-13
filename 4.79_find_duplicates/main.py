#So, I stopped the video before he said "by the way, you cannot use Sets."
#So the commented chunk is a better solution using Sets

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'n']

# non_duplicates = set()

# duplicates = set()

# for item in some_list:
#   if item not in non_duplicates:
#     non_duplicates.add(item)
#   else:
#     duplicates.add(item)

# print('The following duplicates were found in the list: ' +
#       (', '.join(sorted(duplicates))))

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'n']

duplicates = []

for item in some_list:

  counter = 0
  for letter in some_list:
    if item is letter:
      counter += 1

    if counter > 1 and item not in duplicates:
      duplicates.append(item)
      break

print('The following duplicate letters were found: ' + ', '.join(duplicates))