#!/usr/bin/python
import socket
import logging
import base64

def decode(s):
    s=base64.b64decode(s)
    s=s[:-7]+chr(ord(s[-7])-1)+s[-6:-5]+chr(ord(s[-5])-1)+s[-4:-3]+chr(ord(s[-3])-1)+s[-2:-1]+chr(ord(s[-1])-1)
    return s

show_only_changed=True
#log_format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
log_format='%(asctime)s %(message)s'
if __name__=='__main__':
    #config log->file and console
    logging.basicConfig(level=logging.INFO,format=log_format,datefmt='%a, %d %b %Y %H:%M:%S',filename='server.log',filemode='w')
    console=logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    #open socket
    flags={}
    address=('0.0.0.0',55168)
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(address)
    logging.info("Server starting,listening on port 55168...")
    while 1:
        data,addr=s.recvfrom(2048)
        if data:
            data=decode(data)
            if not show_only_changed or  flags.get(addr[0])!=data:
                flags[addr[0]]=data
                msg= "[ From "+addr[0]+' ] '+data
                logging.info(msg)
    s.close()
