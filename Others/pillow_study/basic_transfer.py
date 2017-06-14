#!/usr/bin/env python
# Funtion:      
# Filename:

from PIL import  Image

baby = Image.open("1.jpg")
x,y = baby.size
sqaure_baby = baby.resize((250, 250))

baby.show()
sqaure_baby.show()