# Standard way to open existing file for reading. Using with open... you don't need cose.
with open('test.txt') as my_file:
    print(my_file.readlines())

# mode='w' will open file for writing
# This will open existing file and set cursor to position 0, then begin overwriting.
# This will create a new file as well, if it does not exist.

# mode='r+' will open for reading and writing

# mode='a' will open the file for appending

# https://docs.python.org/3.8/tutorial/inputoutput.html#reading-and-writing-files