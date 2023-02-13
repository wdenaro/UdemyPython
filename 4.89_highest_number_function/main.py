# This was my solution for the problem. If I knew the incoming
# list was potentially to be 100's or thousands of items, I would have
# taken a different approach


def highest_even(li):

  highest = 0

  for val in li:
    if val > highest and val % 2 == 0:
      highest = val

  return highest


print(highest_even([10, 2, 3, 90, 4, 8, 11]))

# The instructors solution


def highest_even2(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)

  return max(evens)


print(highest_even2([10, 2, 3, 90, 4, 8, 11]))