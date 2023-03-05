# pip3 import Pillow
# https://pillow.readthedocs.io/en/stable/

from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')

filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save('pikachu_blur.png', 'png')

filtered_image = img.filter(ImageFilter.SMOOTH)
filtered_image.save('pikachu_smooth.png', 'png')

filtered_image = img.convert('L')
filtered_image.save('pikachu_gray.png', 'png')

print(img)

print(img.format)

print(img.size)

print(img.mode)

print(dir(img))

