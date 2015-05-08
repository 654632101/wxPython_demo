# -*- encoding:utf-8 -*-
import os, Image

def binary(f):                #图像的二值化处理
    print f
    img = Image.open(f)
    #img = img.convert('1')
    img = img.convert("RGBA")  #参考文章中无该行，无该行，我这里会报错
    pixdata = img.load()
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
    return img
nume = 0
def division(img):        #图像的分割，就是验证码按字符分割出来
    global nume
    font=[]
    for i in range(4):
        x = 9 + i*20  #这里的数字参数需要自己
        y = 9
        temp = img.crop((x,y,x+12,y+15))
        temp.save("D:/workspace/py_demo/com/king/captcha/temp/%d.gif" % nume)
        nume=nume+1
        font.append(temp)
    return font
def recognize(img):        #分隔出来的字符与预先定义的字体库中的结果逐个像素进行对比找出差别最小的项
    fontMods = []
    path = os.getcwd()
    print '路径是 : %s', path
    for i in range(1,10):
        fontMods.append((str(i), Image.open("D:/workspace/py_demo/com/king/captcha/fonts/%d.gif" % i)))
    result=""
    font=division(img)
    for i in font:
        target=i
        points = []
        for mod in fontMods:
            diffs = 0
            for yi in range(15):
                for xi in range(12):  #以下多行为自己修改，参考文章中的值对比存在问题
                    if 0 in target.getpixel((xi, yi)):
                        compare = 0
                    else:
                        compare = 255
                    if mod[1].getpixel((xi, yi)) != compare:
                        diffs += 1
            points.append((diffs, mod[0]))
        points.sort()
        result += points[0][1]
    return result
if __name__ == '__main__':
    codedir="./pic/"
    for imgfile in os.listdir(codedir):
        if imgfile.endswith(".jpg"):
            dir="./result/"
            print codedir+imgfile
            img=binary(codedir+imgfile)
            print img
            num=recognize(img)
            dir += (num+".jpg")
            print "save to", dir
            img.save(dir)