my_list = [5, 4, 3]

# Challenge #1 Square the list
print(list(map(lambda item: item**2, my_list)))

# Challenge #1 Sort list by second item in each tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)