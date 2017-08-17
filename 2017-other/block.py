from PIL import Image

im=Image.open(r'stego_100.png')
small=''
print im.mode,im.size
m1=m2=''
for x in range(19):
    for y in range(19):
        r,g,b,a=im.getpixel((171+y,171+x))
        if(a==254):
            small+='0'
        elif(a==255):
            small+='1'
print small
im=im.convert("1")
large=''
for x in range(19):
    for y in range(19):
        color=im.getpixel((19*y,19*x))
        large+='1' if color==255 else '0'
print large
xor=''
for i in range(len(small)):
    xor+='0' if small[i]==large[i] else '1'
print xor
print ''.join(chr(int(xor[i:i+8],2)) for i in range(0,len(xor),8))
