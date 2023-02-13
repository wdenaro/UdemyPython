# Performance Decorator
from time import time


def performance(func):

  def wrap_func(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()
    print(f'It took {t2 - t1} s')
    return result

  return wrap_func


@performance
def long_time():
  for i in range(1000000):
    i * 5

  print('Done')


long_time()