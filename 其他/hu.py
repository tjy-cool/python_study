#!/usr/bin/env python
# Funtion:      
# Filename:

import os, sys
# import caffe
# import numpy as np
# import matplotlib.pyplot as plt
from random import Random
# import skimage.io as io
data_dir='c:/Users/li/Desktop/zhache/test/uncovered'
str0=data_dir + '/*.jpg'
# coll = io.ImageCollection(str0)
base_path = r'F:/demo-grand/bio_sample/bio_pythondemo/'
if not os.path.exists(base_path):
    for i in range(1, 5):
         # 将该序号转换成对应的类别名称，并打印
        class_name = {1: 'building', 2: 'canvas', 3: 'car', 4: 'cement', 5: 'uncovered'}
        num = Random()
        path = base_path + class_name[i]
        os.makedirs(path)
        print("fsf")
