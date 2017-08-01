# -*- coding: utf-8 -*-

import binascii
import base64
import string
import itertools
import zipfile
import struct
#str和其他二进制数据类型的转换#>>> struct.pack('>I', 10240099)#'\x00\x9c@c'

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/='

crcdict = {}
print "computing all possible CRCs..."
for x in itertools.product(list(alph), repeat=4):
    st = ''.join(x)
    testcrc = binascii.crc32(st)  # CRC 值域為 [-2^31, 2^31-1] 之間的有號整數
    crcdict[struct.pack('<i', testcrc)] = st  #转化为字节流
print "Done!"

b64data = ""
for i in range(54):
    print i
    f = open('chunk{0}.zip'.format(i))
    data = f.read()
    f.close()
    crc = ''.join(data[14:18]) #crc32校验值在14-18
    if crc in crcdict:
        b64data+=crcdict[crc]
        print crcdict[crc]
    else:
        print "FAILED!"

print b64data

print "writing b64 to file"
out = open('out.zip', 'w')
dec = base64.b64decode(b64data)
out.write(dec)
out.close()

print "Brute forcing ZIP pass"
with zipfile.ZipFile('out.zip', 'r') as myzip:
    for i in range(1,5):
        for x in itertools.product(list(alph), repeat=i):
            pwd = ''.join(x)
            try:
                myzip.extract('flag.txt', './',pwd)
                break
            except:
                pass
        else:
            continue
        break
    myzip.close()
    flag = open('flag.txt')

print "flag:"
print flag.read()
flag.close()
