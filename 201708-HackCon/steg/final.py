import base64
from PIL import Image
data=open(r'final.png','rb').read()
_h=r'iVBORw0KG'
p=data.find(_h)
f=r'final/final%d.png'
i=0
while(-1!=p):
    #print p
    open(f%(i),'wb').write(data[:p])
    data=data[p:]
    data=base64.b64decode(data)
    p=data.find(_h)
    i+=1
open(f%(i),'wb').write(data)
x,y=0,0
im=Image.new('RGB',(28*6,34*5))
for y in range(5):
    for x in range(6):
        _frag=Image.open(f%(y*6+x))
        im.paste(_frag,(x*28,y*34))
im.show()