# Exercise: Return a list of only the duplicates from some_list
# using a comprehension

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = [value for value in set(some_list) if some_list.count(value) > 1]

print(duplicates)

# again, I feel like my solution is cleaner than the instructors
# duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
# print(duplicates)