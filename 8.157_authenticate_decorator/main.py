# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
  'name': 'Sorna',
  'valid':
  False  # changing this will either run or not run the message_friends function.
}


def authenticated(func):

  def wrap_func(*args, **kwargs):
    if user1['valid']:
      return func(*args, *kwargs)
    else:
      print(f'Sorry, your request failed to authenticate.')

  return wrap_func


@authenticated
def message_friends(user):
  print('Message has been sent')


message_friends(user1)