<?php

// Monitor configuration

return array(
	 	 //【C1】WLOG, set variable for capture.php(流量监控)
	 'wlog_dir'   => '/home/user/lg/', 
    //【C2】attack_LOG, set variable for capture.php（waf）
    'attacklog_dir' => '/home/user/lg/',
		//【C3】fsmon.php的配置项, set variables for fsmon.php
		//用于指定遍历根目录(绝对路径)
	 'root'   => '/var/www/html/',
		//检测时间间隔(单位us，1s=1000 000 us)
	 'interval' => 50000,
	 //用于指定存放文件监控日志的目录(绝对路径)
	 'log_dir'   => '/var/www/html/youneverknownhuxiao/fsmon/',
     // allowed multi root
     // 'root' => ['/first', '/second', ...]

     //'root' => array(
     //   __DIR__ . '\\1',
     //   __DIR__ . '\\2'
     //),

     // skip this dirs
     //'ignore_dirs' => [
     // '/home/decoder/',
	//'/home/ubuntu/',
	//'/home/xctf/'
     //],

     // ServerTag for text reports, default _SERVER[SERVER_NAME]
	 // 'server' => 'server_name',

     // files pattern
	 'files' => '(\.php.?|\.htaccess|\.txt |\.py |\.sh)$',

      // write logs to ./logs/Ym/d-m-y.log
     'log' => true,

      // notify administrator email
	 'mail' => array(
	 	'from'   => '123@123.ru',
	 	'to'   	 => '123@gmail.com',

	 	// disabled by default
	 	'enable' => false
	 )

);
