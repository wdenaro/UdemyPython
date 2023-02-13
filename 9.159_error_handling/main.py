# Error Handling exercise
# Reference
# https://docs.python.org/3.8/library/exceptions.html

while True:
  try:
    age = int(input('What is your age? '))
    10 / age
  except ValueError:
    print('Please enter a number')
  except ZeroDivisionError:
    print('Please enter age higher than 0')
  else:
    print('Thank you')
    break