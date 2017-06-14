#!/usr/bin/env python
# Funtion:      
# Filename:

from PIL import Image
img = Image.open("1.jpg")
area = (100, 100, 500, 500)
cropped_img = img.crop(area)
print(cropped_img.size)
cropped_img.show()

