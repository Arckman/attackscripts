'''
a=open('chall.ino.hex')
b=open('output','w')
for l in a.readlines():
    b.write(l[9:])
'''

#-----------convert to bitmap

from PIL import Image,ImageDraw
im=Image.new('1',(16*34,996))
#draw=ImageDraw.Draw(im)
lines=open('output','r').readlines()
row,col=0,0
pixels=im.load()
for l in lines:
    #print('row:%s'%(row,))
    for i in range(0,len(l)-1,2):
        #print l[i:i+2]
        n=int(l[i:i+2],16)
        for i in range(0,8):
            #print 'col:%s'%(str(col),)
            x=n&(128>>i)
            #draw.bitmap()
            if x==0:
                pixels[col,row]=0
            else:
                pixels[col,row]=1
            col+=1
    row+=1
    col=0
im.show()
#im.save('result.jpg')
