# Set Comprehensions

# Create a set from the unique characters in the string provided
my_set = {char for char in 'hello'}
print(my_set)

# Create a set using the results in the range
my_set2 = {num for num in range(0, 100)}
print(my_set2)

# Create a set using the range results to the power of 2
my_set3 = {num**2 for num in range(0, 100)}
print(my_set3)

# Dictionary Comprehensions

# Create a new list that keeps the keys the same, but the values are to the power of 2
simple_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict = {
  key: value**2
  for key, value in simple_dict.items() if value % 2 != 0
}
print(my_dict)

# Create a dictionary where number in provided list is the key and the value is 10-times the number
my_dict2 = {num: num * 10 for num in [1, 2, 3, 4]}
print(my_dict2)