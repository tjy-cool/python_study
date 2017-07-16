#!/usr/bin/env python
# Funtion:      
# Filename:
from PIL import Image
sister = Image.open("sister.jpg")
girl = Image.open("girl.png")
area = (100, 100, 300, 300)
sister.paster(girl, area)
sister.show()
