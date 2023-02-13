# Fibonacci Generator
def my_func(num):
    a = 0
    b = 1

    for i in range(num):
        yield a
        fib = a + b
        a = b
        b = fib


for each_fib in my_func(21):
    print(each_fib)