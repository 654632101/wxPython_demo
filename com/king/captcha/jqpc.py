#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#图像分割
import os ,Image
j = 1
dir="./conf/"
for f in os.listdir(dir):
    if f.endswith(".jpg"):
        print dir+f
        img = Image.open(dir+f)
        for i in range(4): 
            x = 9 + i*20  #这里的数字参数需要自己
            y = 9
            print x
            print y          #根据验证码图片的像素进行
            img.crop((x, y, x+12, y+15)).save("fonts/%d.gif" % j)   #适当的修改
            print "j=",j 
            j += 1