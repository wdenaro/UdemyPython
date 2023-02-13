# Pure Functions
# 1. Always returns same/reliable results
# 2. Does not affect outside world


def multiply_by2(li):

  new_list = []

  for item in li:
    new_list.append(item * 2)
  return new_list


print(multiply_by2([123, 246, 369]))