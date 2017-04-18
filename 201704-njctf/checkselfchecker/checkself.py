import os
import logging
import re
import sys

path=r'C:\Users\szgd\Desktop\njcms\njcms'
#l=logging.DEBUG
l=logging.INFO
logging.basicConfig(level=l,format='%(asctime)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

def check(path):
    for dirpath,dirnames,filenames in os.walk(path):
        logging.debug(dirpath)
        logging.debug(dirnames)
        logging.debug(filenames)
        for f in filenames:
            if re.match('.*\.php$',f):
                for line in open(dirpath+os.path.sep+f).readlines():
                    if re.match(".*REQUEST\['checker'\].*",line):
                        logging.info('{'+f+'} '+line)

check(path)
