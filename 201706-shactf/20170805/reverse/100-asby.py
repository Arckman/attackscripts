v18=['\x10', ' ', '\x15', 'D', 'S', 'b', '\x14', '3', 'j', '}', '\xf7', '\xc5', '\xab', '\xa7', '\x12']
v34='764c742328522607081c96fdcac42223457376610470570f4bc6a69bc1232110237d3550724e'.decode('hex')

xor=lambda a,b:chr(ord(a)^ord(b))
l=len(v18)
re=''
for i,c34 in enumerate(v34):
    c18=v18[i%l]
    re+=xor(c18,c34)

print re