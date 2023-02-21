# Translator exercise

# I Googled this...
from translate import Translator

_file = 'lipsum.txt'

translator = Translator(to_lang="German")

try:
    with open(_file, mode='r') as lipsum:

        # One word at a time, slower but way cooler looking!
        # words = lipsum.read().split()
        #
        # for word in words:
        #     translation = translator.translate(word)
        #     print(translation, end =" ")

        text = lipsum.read()
        translation = translator.translate(text)

        with open('./german.txt', mode='w') as outfile:
            outfile.write(translation)

            print('Translated file written, have a knife day.')

except FileNotFoundError as err:
    print(f'Could not locate {_file}')
    raise err

except IOError as err:
    print('Some sore of I/O error has occured, get bent')
    raise err
