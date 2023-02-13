# List Comprehensions

# the long way (yet very readable)
my_list = []

for char in 'hello':
  my_list.append(char)

print(my_list)

# the list comprehension way
my_list1 = [char for char in 'HELLO']
print(my_list1)

# examples

#          list comprehension
#          [ var | loop through iterable ]
my_list2 = [num for num in range(0, 100)]
print(my_list2)

#          [ expression | loop through iterable ]
my_list3 = [num**2 for num in range(0, 100)]
print(my_list3)

#          [ expression | loop through iterable | conditional ]
my_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]
print(my_list4)