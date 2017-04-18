<?php
/**
 * Created by PhpStorm.
 * User: szgd
 * Date: 2016/7/24
 * Time: 9:39
 */
$dir=dirname(__FILE__);
//echo is_dir($dir);
function touchfile($basedir,$dir){
    if(false!==($handle=opendir($basedir.DIRECTORY_SEPARATOR.$dir))){
        while(false!==($file=readdir($handle))){
            if($file!='.'&&$file!='..'){
                if(is_dir($basedir.DIRECTORY_SEPARATOR.$dir.DIRECTORY_SEPARATOR.$file)){
                    touchfile($basedir,$dir.DIRECTORY_SEPARATOR.$file);
                }
                else if(preg_match('/\.php[1-6]?$/i',$file))
                    echo $basedir.DIRECTORY_SEPARATOR.$dir.DIRECTORY_SEPARATOR.$file.'</br>';
                    //touch($basedir.DIRECTORY_SEPARATOR.$dir.DIRECTORY_SEPARATOR.$file);
            }
        }
    }
}
//touchfile($dir.'/../','');
touchfile($dir,'');



?>