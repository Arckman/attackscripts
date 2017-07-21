import os
r=''
#for path,d,files in os.walk('/tmp/mnt'):
#	for f in files:
#		r+=open(path+'/'+f).read()
for i in range(0,254):
	if os.path.isfile('/tmp/mnt/'+str(i)):
		r+=open('/tmp/mnt/'+str(i)).read()
print r
	

