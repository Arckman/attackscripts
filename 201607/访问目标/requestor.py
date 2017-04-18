#coding:gb2312

import requests
import multiprocessing
import time
import urllib
import logging

#sleeptime=0.1
loggingLevel=logging.INFO
#loggingLevel=logging.WARNING
logging.basicConfig(level=loggingLevel,format='%(asctime)s %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

def request(target,urls):
    global sleeptime
    logging.debug('starting requesting '+target)
    for u in urls:
        url='http://'+target+'/'+urllib.quote(u)
        logging.info('hitting url['+url+']')
        try:
            requests.post(url,timeout=0.05)
        except:
            logging.debug("Error in hitting "+url)
        #time.sleep(sleeptime)

if __name__=='__main__':
    print "starting..."
    file=open(r'targets.txt','rt')
    file2=open(r'all_a.txt','rt')
    urls=[]
    targets=[]
    for line in file:
        targets.append(line.strip())
    for line in file2:
        urls.append(line.strip())
    file.close()
    file2.close()
    if len(targets)!=0:
        #p=multiprocessing.Process(target=request,name='request',args=(targets,urls))
        logging.info('Initing Process Pool doing requesting...')
        p=max(4,len(targets))
        pool=multiprocessing.Pool(processes=p)
        for target in targets:
            pool.apply_async(request,(target,urls))
        pool.close()
        pool.join()
    logging.info('Request END!!')
