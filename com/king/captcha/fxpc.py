#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#图像二值处理
import os
from PIL import Image
j=1
dir="./pic/"
path = "./conf/"
for f in os.listdir(dir):
    if f.endswith(".jpg"):
        print dir+f
        img = Image.open(dir+f) # 读入图片
        img = img.convert("RGBA")
        pixdata = img.load()
        print img.size[0]
        print img.size[1]
        #二值化
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][0] < 90:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][1] < 136:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][2] > 0:
                    pixdata[x, y] = (255, 255, 255, 255)
        print path+f           
        img.save(path+f, "GIF")