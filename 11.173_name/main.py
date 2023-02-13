from utility import multiply, divide
from shopping.more_shopping.shopping_cart import buy


# Call any function in utility like this
print(multiply(2, 3))

print(divide(200, 420))

print(buy('apple'))

# See results of print statements in this file and 2x imported files
print(__name__)


# Execute block only if this file is the current script being run (as
# opposed to imported
if __name__ == '__main__':
    # do something
    pass