#coding:u8

#import psutil
import multiprocessing
from multiprocessing import Pipe
import time


class Worker(multiprocessing.Process):

    def setCon(self,con):
        self.con=con

    def run(self):
        print multiprocessing.current_process().name,'child'
        #print multiprocessing.
        time.sleep(8)


if __name__=='__main__':
    con1,con2=Pipe()
    p1=Worker(args=())
    p1.setCon(con1)
    p1.daemon=False
    p2=Worker(args=())
    p2.daemon=False
    p2.setCon(con2)
    p2.start()
    p1.start()
