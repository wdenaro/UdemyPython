
try:
    with open('sad.vxt', mode='r') as my_file:
        print(my_file.read())

except FileNotFoundError as err:
    print('File does not exist')
    raise err
except IOError as err:
    print('I/O Error')
    raise err
