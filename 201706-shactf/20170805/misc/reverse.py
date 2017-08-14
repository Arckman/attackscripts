
_in=open('reverse','rb')
_out=open('out','wb')
data=_in.read()
data=data[::-1]
out_data=bytearray(len(data))
for i,d in enumerate(data):
    out_data[i]=chr(((ord(d)&0xf)<<4)|((ord(d)&0xf0)>>4))
_out.write(out_data)
_out.close()