# https://unsplash.com/s/photos/apollo-11

from PIL import Image, ImageFilter

img = Image.open('./images/astro.jpg')
# print(img.size)

# new_img = img.resize((400, 200))
# new_img.save('./images/astro_thumb.jpg')
# print(img.size)

img.thumbnail((400, 400))
img.save('./images/astro_thumb.jpg')
print(img.size)