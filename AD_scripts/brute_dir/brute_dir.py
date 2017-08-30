#coding:utf-8
import requests
import time
import logging

input_Filename_target = "target.txt"
ports = ['80']
input_Filename_dic = "PHP.txt"
interval = 0.1  # 延迟(秒)

target = []
dic = []

mode='development'
#mode='product'
if mode=='development':
	loglevel=logging.DEBUG
	log_format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
elif mode=='product'
	loglevel=logging.INFO
	log_format='%(asctime)s %(message)s'

logging.basicConfig(level=loglevel,format=log_format,datefmt='%a, %d %b %Y %H:%M:%S',)

with open(input_Filename_target,'r') as input_File_target:
	target = input_File_target.readlines()
with open(input_Filename_dic,'r') as input_File_dic:
	lines = input_File_dic.readlines()

while(True):
	dic=iter(lines)
	for path in dic:
		for port in ports:
			port='' if port=='80' else ':'+port
			for ip in target:
				try:
					url = "http://%s%s%s"%(ip.strip(),port,path.strip())
					logging.debug('Accessing %s'%(url,))
					requests.get(url,timeout=1)			
				except:
					logging.info("Unable connect to URL: http://%s%s"%(ip.strip(),port))
			time.sleep(interval)

