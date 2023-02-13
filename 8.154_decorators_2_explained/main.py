# Decorator


# Define this function, which will be used as a decorator
def my_decorator(func):

  def wrap_func():
    print('*********')
    func()
    print('*********\n')

  return wrap_func


# Preceed new function with decorator, it's like handing this function off
# to the above function
@my_decorator
def hello():
  print('hellllooo')


hello()


@my_decorator
def bye():
  print('goodbye!')


bye()