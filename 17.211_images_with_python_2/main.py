from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.save('pikachu_rotated.png', 'png')
# filtered_img.show()

# rotated = filtered_img.rotate(-90)
# rotated.show()

# thumb = filtered_img.resize((75, 75))
# thumb.show()

crop_box = (100, 100, 400, 400)
cropped = filtered_img.crop(crop_box)
cropped.show()
