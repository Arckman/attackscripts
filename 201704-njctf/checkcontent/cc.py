import os
import sys
import logging
import re

l=logging.DEBUG
#l=logging.INFO
logging.basicConfig(level=l,format='%(asctime)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

if len(sys.argv) >=3 and len(sys.argv)<=4:
    path=sys.argv[-2]
    pattern=sys.argv[-1]
    logging.debug(path)
    logging.debug(pattern)
    try:
        for dirpath,dirnames,filenames in os.walk(path):
            for f in filenames:
                for line in open(dirpath+os.path.sep+f).readlines():
                    if re.match(".*"+pattern+".*",line):
                        logging.info('{'+dirpath+os.path.sep+f+'}@@'+line)
    except Exception as e:
        logging.debug(e.message)
