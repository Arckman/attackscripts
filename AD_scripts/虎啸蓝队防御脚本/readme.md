虎啸版蓝队防御脚本

目录说明：
./
|
+-dist/		#包含各种防御脚本，和编译好的x64版本inotifytools、rsync
|   |
|   +-z1/	#包含编译好的x64版本inotifytools、rsync
|
+-dept/		#包含一些Php的流量监控和waf

文件说明：
dist/init.sh 	#调整所有脚本可执行权限
dist/0*.sh		#服务器信息收集，获取各类中间件和cms信息，find版本和locate版本
dist/1bak.sh	#文件备份脚本
dist/1iwatch.sh		#利用inotify、rsync的实时防篡改脚本
dist/1*.sh（除上述两个外）	#利用while循环、rsync的实时防篡改脚本
dist/3*.sh 		#所有网页插入php include，用于流量监控和waf
dept/capture.php 	#流量监控和waf的php
dept/fsmon.php 		#文件监控的php
dept/myconf.php 	#设置了一些（上面两个文件）php的变量

使用说明：
1.先用0*.sh查看系统中中间件和cms信息；
2.使用1bak.sh备份指定文件目录；
3.选用inotify实现版本或者while循环实现版本，启动文件实时放篡改；
4.用3*.sh架设waf和流量监控；
5.其他后期命令可加入9*.sh中。