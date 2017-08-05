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
