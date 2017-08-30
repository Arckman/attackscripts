import random
lines=open(r'_PHP.txt').readlines()
print len(lines)
_out=[]
for l in lines:
    _out.append(l)
    pice=l.split('/')
    pice[-1]='.'+pice[-1]
    _out.append('/'.join(pice))
print len(_out)
random.shuffle(_out)
_w=open(r'PHP.txt','w')
for l in _out:
    _w.writelines(l)