import os
from PIL import Image
xx = 1000
yy = 1000
'''
from PIL import Image
im = Image.open("sample-image.png")

angle = 45 
out = im.rotate(angle) 
out.save('rotate-output.png')
'''

curdir = os.path.abspath(os.curdir)
for current_dir,dirs ,files in os.walk("img_in"):  #передаем в качестве аргумента директорию из тек. папки
    n = 0
    for in_file in files:
        n = n +1
        fi_in = curdir+'\\img_in\\'+in_file
        fi = str(n)+'.jpg'
        print(in_file,fi)
        fi_out = curdir+'\\img_out\\'+fi
        #print(fi)
        im = Image.open(fi_in)
        #im = im1.rotate(90)

        x = im.size[0]
        y = im.size[1]
        size = (x, y)
        if x > y:
            print("1",x,y)
            if x > xx:
                k = x / xx
                y1 = int(y / k)
                size = (xx, y1)
        else:
            print("2",x,y)
            if y > yy:
                k = y / yy
                x1 = int(x / k)
                size = (x1,yy)
                print(size[0],size[1])
        out = im.resize(size)
        out.save(fi_out)
