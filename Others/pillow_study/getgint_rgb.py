#!/usr/bin/env python
# Funtion:      
# Filename:

from PIL import Image

sister = Image.open("1.jpg")
print(sister.mode)      # RGB

r, g, b = sister.split()    #
# r.show()
# g.show()
# b.show()

new_img = Image.merge("RGB",(r,g,g))
new_img.show()
