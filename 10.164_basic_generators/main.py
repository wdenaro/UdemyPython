# Generators Explained

# def generator_func(num):
#     for i in range(num):
#         yield i
#
#
# for item in generator_func(1000):
#     print(item)


def generator_func2(num):
    for i in range(num):
        yield i * 2


g = generator_func2(1000)
next(g)
next(g)
print(next(g))