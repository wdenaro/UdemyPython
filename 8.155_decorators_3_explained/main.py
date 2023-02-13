# Decorator Pattern with multiple arguments and keyword arguments


# Define this function, which will be used as a decorator
def my_decorator(func):

  def wrap_func(*args, **kwargs):
    print('****************')
    func(*args, **kwargs)
    print('*' * len(args[0]) + '\n')

  return wrap_func


# Preceed new function with decorator, it's like handing this function off
# to the above function
@my_decorator
def hello(greeting, emoji=':-)'):
  print(greeting, emoji)


hello('Hello my friend.')