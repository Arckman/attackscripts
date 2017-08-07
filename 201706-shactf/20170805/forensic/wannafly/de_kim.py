#!encoding:utf8
'''
script for shactf2017/forensic-100/WannaFly
'''
from PIL import Image
from Crypto.Cipher import AES
import os
import random,string,base64

k=r'Hb8jnSKzaNQr5f7p'
def getImages(path=r'.'):
    i=[]
    for p,d,f in os.walk(path):
        for x in f:
            if x.endswith('png'):
                i.append(x)
    return i

def getIV(f):
    stat=os.stat(f)
    t=stat.st_mtime
    random.seed(int(t))
    iv=""
    for i in range(16):
        iv+=random.choice(string.letters+string.digits)
    return iv

def findoldim(f):
    im=open(f,'rb').read()
    im=im[im.find("IEND")+9:]
    return im

def decrypt(k,m,iv):
    cipher=AES.new(k,AES.MODE_CFB,iv)
    return cipher.decrypt(base64.b64decode(m))

for f in getImages():
    print "process...:%s"%f
    iv=getIV(f)
    m=findoldim(f)
    oldim=decrypt(k,m,iv)
    old,ext=os.path.splitext(f)
    n=old+"_new"+ext
    i=Image.open(f)
    # len(oldim)
    # im=Image.frombytes(i.mode,i.size,oldim)
    # im.show()
    im=open(n,'wb')
    im.write(oldim)
    im.close()

