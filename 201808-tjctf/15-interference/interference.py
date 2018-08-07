from PIL import Image

v1=Image.open('v1.png')
v2=Image.open('v2.png')
assert(isinstance(v1,Image.Image))
print(v1.format,v1.size,v1.mode)
v3=Image.new('RGBA',(300,300))
v4=Image.new('RGBA',(300,300))

for i in range(300):
    for j in range(300):
        p1=v1.getpixel((i,j))
        p2=v2.getpixel((i,j))
        v3.putpixel((i,j),(p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2],255))
        v4.putpixel((i,j),(-p1[0]+p2[0],-p1[1]+p2[1],-p1[2]+p2[2],255))
v3.save('v3.png')
v4.save('v4.png')
