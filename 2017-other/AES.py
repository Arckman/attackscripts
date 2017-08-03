'''
demo for Crypto.Cipher.AES
'''
from Crypto.Cipher import AES
import base64
c='h2ly95ZTM0nm3Vp+3FbNdNOw5E5MXQ8yp+eYLHn9b8M='
k=b'2016063020160630'

def en(t,k):
    cipher=AES.new(k)
    #len(key) determines aes-128/192/256
    #default mode is ecb
    #iv is ignored when ecb
    t2=padding(t,k)
    c=cipher.encrypt(t2)
    c=base64.b64encode(c)
    return c
def de(c,k):
    cipher=AES.new(k)
    c=base64.b64decode(c)
    c2=padding(c,k)
    t=cipher.decrypt(c2)
    return t

def padding(s,k):
    l=len(k)
    return s+(l-len(s)%l)*' '

if __name__=='__main__':
    print de(c,k)[:16]
    print en('l0v3_a.1.chann3I',k)
