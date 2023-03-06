""" From command line % JPGtoPNGconverter.py <Source_folder/> <destination_folder/>
    """

import sys
import os
from PIL import Image

# grab first and second arguments
try:
    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
except:
    print('Must have two arguments <source/> and <destination/>')


# check if second argument exists as a folder, if not create
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)


# loop through source folder
for image_file in os.listdir(source_folder):
    name_only = os.path.splitext(image_file)[0]
    full_image_path = os.path.join(source_folder, image_file)
    if os.path.isfile(full_image_path):
        #print(full_image_path)

        img = Image.open(full_image_path)
        try:
            img.save(f'{destination_folder}{name_only}.png', 'png')
        except:
            print('error occurred while saving file')
