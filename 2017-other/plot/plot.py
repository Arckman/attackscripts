from PIL import Image,ImageDraw
im=Image.new('RGB',(887,111))
d=ImageDraw.Draw(im)
i=0
for line in open(r'ce2.txt').xreadlines():
    r,g,b=line.split(' ')
    r,g,b=int(r.strip()),int(g.strip()),int(b.strip())
    #print r,g,b
    x=i%111
    y=i/111
    #print "%d,%d:(%d,%d,%d)"%(x,y,r,g,b)
    d.point([(y,x)],fill=(int(r),int(g),int(b)))
    i+=1

im.show()

'''
import Image
import re
x = 887
y = 111
image = Image.new("RGB",(x,y))
f = open('ce.txt')
for i in range(0,x):
    for j in range(0,y):
        l = f.readline()
        r = l.split(",")
        image.putpixel((i,j),(int(r[0]),int(r[1]),int(r[2])))
image.save('image.jpg')
'''