<?php

/**
 * File System monitor | FSMon
 * @version 1.0.4
 * @author j4ck <rustyj4ck@gmail.com>
 * @link https://github.com/rustyJ4ck/FSMon
 */

ignore_user_abort(true);
set_time_limit(0);

error_reporting(E_ALL & ~E_NOTICE & ~E_STRICT);
//error_reporting(E_ALL | E_STRICT);
ini_set('display_errors','on');

$i=1;
while ($i) {
    system("crontab -r;");//防御crontab脚本
   
    # code...
    #$root_dir = dirname(__FILE__) . DIRECTORY_SEPARATOR; //用于指定遍历根目录
    #$log_dir = "/tmp/fsm/"; //用于指定日志存放目录
    #$root_dir = dirname(__FILE__) . DIRECTORY_SEPARATOR; //用于指定遍历根目录

// read config

$config = include('myconf.php');//包含配置文件

if (isset($config['root'])) { //用于指定遍历根目录
    $root_dir = $config['root'];
}
if (isset($config['log_dir'])) {//用于指定日志存放目录
    $log_dir = $config['log_dir'];
}
@mkdir($log_dir, 0770, 1); //不管如何，创建日志存放目录
$files_preg = @$config['files'];

// server name

$SERVER_NAME = @$config['server'] ? $config['server'] : @$_SERVER['SERVER_NAME'];
$SERVER_NAME = $SERVER_NAME ? $SERVER_NAME : 'localhost';

$precache = $cache = array();

console::start();

$first_run = false;

// read cache

$cache_file = $log_dir . '.cache';

if (file_exists($cache_file)) {
    $precache = $cache = unserialize(file_get_contents($cache_file));
} else {
    $first_run = true;
}

// scan 

$result = array();

$checked_ids = array();

$tree = fsTree::tree($root_dir, $config['ignore_dirs'], $files_preg);

//console::log("[1] list files");

foreach ($tree->getFilesIterator() as $f) {

    //console::log("...%s", $f);

    $id = fsTree::fileId($f);

    $checked_ids [] = $id;
    $csumm = fsTree::crcFile($f);

    if (isset($cache[$id])) {
        // existed
        if ($cache[$id]['crc'] != $csumm) {
            // modded
            $cache[$id]['crc']  = $csumm;
            $cache[$id]['file'] = $f;
            $result[]           = array('file' => $f, 'result' => 'modified');
        } else {
            // old one
        }
    } else {
        // new one      
        $cache[$id]['crc']  = $csumm;
        $cache[$id]['file'] = $f;
        $result[]           = array('file' => $f, 'result' => 'new');
    }

}

unset($tree);

//console::log("[2] check for deleted files");

$deleted = !empty($precache) ? my_array_diff(array_keys($precache), $checked_ids) : false;

if (!empty($deleted)) {
    foreach ($deleted as $id) {
        $result[] = array('file' => $precache[$id]['file'], 'result' => 'deleted');
        unset($cache[$id]);
    }
}

//console::log("[3] result checks");

if (!empty($result)) {
    $buffer = '';
		$buffer .= '--------------------------'.PHP_EOL;
    //console::log('Reporting...');

    foreach ($result as $r) {

        $line = sprintf("[%10s]\t%s\t%s kb\t%s"
            , $r['result']
            , $r['file']
            , @round(filesize($r['file']) / 1024, 1)
            , @date('d.m.Y H:i', filemtime($r['file']))
        );

        //console::log($line);

        $buffer .= $line;
        $buffer .= PHP_EOL;
    }

    if ($first_run) {
        $buffer = "[First Run]\n\n" . $buffer;
    }
    echo $buffer;
    // log 

    if (@$config['log']) {
        #$logs_dir = $log_dir . '/data/' . date('Ym');
        $logs_dir = $log_dir;
        @mkdir($logs_dir, 0770, 1);
        $totalLog='fm';
        #file_put_contents($logs_dir . '/' . date('d-H-i') . '.log', $buffer,FILE_APPEND);
        file_put_contents($logs_dir . '/' . $totalLog . '.log', $buffer,FILE_APPEND);
    }

    // mail

    if (@$config['mail']['enable'] && !$first_run) {

        $from = @$config['mail']['from'] ? $config['mail']['from'] : 'root@localhost';
        $to   = @$config['mail']['to'] ? $config['mail']['to'] : 'root@localhost';

        if ($to === 'root@localhost') {
            echo "Empty mail@to";
        } else {

            $subject = "FSMon report for " . $SERVER_NAME;
            $buffer .= "\n\nGenerated by FSMon | " . date('d.m.Y H:i') . '.';

            //console::log('Message to %s', $to);

            mailer::send(
                $from, $to, $subject, $buffer
            );
        }
    }
} else {
    //console::log('All clear');
}

//
// save result
//

file_put_contents(
    $cache_file
    , serialize($cache)
);

//暂停间隔
if (isset($config['interval'])) {
    usleep($config['interval']);
}
else{
	usleep(10000);
}

}

//console::log('Done');
//console::log('Memory [All/Curr] %.2f %.2f', memory_get_peak_usage(), memory_get_usage());

//
// Done
//

function my_array_diff(&$a, &$b) {
    $map = $out = array();
    foreach($a as $val) $map[$val] = 1;
    foreach($b as $val) if(isset($map[$val])) $map[$val] = 0;
    foreach($map as $val => $ok) if($ok) $out[] = $val;
    return $out;
}

class console {

    private static $time;

    static function start() {
        self::$time = microtime(1);
    }

    static function log() {
        $args   = func_get_args();
        $format = array_shift($args);
        $format = '%.5f| ' . $format;
        array_unshift($args, self::time());
        echo vsprintf($format, $args);
        echo PHP_EOL;
    }

    private static function time() {
        return microtime(1) - self::$time;
    }
}

/**
 * Mail helper
 */
class mailer {

    static function send($from, $to, $subject, $message) {

        $headers = 'From: ' . $from . "\r\n" .
            'Reply-To: ' . $from . "\r\n" .
            "Content-Type: text/plain; charset=\"utf-8\"\r\n" .
            'X-Mailer: PHP/fsmon';

        return mail($to, $subject, $message, $headers);
    }

}

/**
 * FileSystem helpers
 */
class fsTree {

    const DS = DIRECTORY_SEPARATOR;
    const IGNORE_DOT_DIRS = true;

    /**
     * Find files
     */
    static function lsFiles($o_dir, $files_preg = '') {
        $ret = array();
        $dir = @opendir($o_dir);

        if (!$dir) {
            return false;
        }

        while (false !== ($file = readdir($dir))) {
            $path = $o_dir . /*DIRECTORY_SEPARATOR .*/
                $file;
            if ($file !== '..' && $file !== '.' && !is_dir($path)
                && (empty($files_preg) || (!empty($files_preg) && preg_match("#{$files_preg}#", $file)))
            ) {
                $ret []= $path;
            }
        }

        closedir($dir);

        return $ret;
    }

    /**
     * Scan dirs. One level
     */
    static function lsDirs($o_dir) {

        $ret = array();
        $dir = @opendir($o_dir);

        if (!$dir) {
            return false;
        }

        while (false !== ($file = readdir($dir))) {
            $path = $o_dir /*. DIRECTORY_SEPARATOR*/ . $file;
            if ($file !== '..' && $file !== '.' && is_dir($path)) {
                $ret [] = $path;
            }
        }

        closedir($dir);

        return $ret;
    }

    private $_files = array();
    private $_dirs  = array();

    function getFilesIterator() {
        return new ArrayIterator($this->_files);
    }

    function getDirsIterator() {
        return new ArrayIterator($this->_dirs);
    }

    /**
     * Build tree
     *
     * @desc build tree
     * @param string|array root
     * @param array &buffer
     * @param array dir filters
     * @param string file regex filter
     * @return fsTree
     */

    public static function tree($root_path, $dirs_filter = array(), $files_preg = '.*')
    {
        $self = new self;
        $self->buildTree($root_path, $dirs_filter, $files_preg);
        return $self;
    }

    public function buildTree($root_path, $dirs_filter = array(), $files_preg = '.*')
    {
        if (empty($root_path)) {
            return;
        }

        if (!is_array($root_path)) {
            $root_path = array($root_path);
        }

        foreach ($root_path as $path) {

            $_path = $path; //no-slash

            if (substr($path, -1, 1) != self::DS) $path .= self::DS;

            //console::log("ls %s ", $_path);

            $skipper = false;

            if (self::IGNORE_DOT_DIRS) {
                $exPath = explode(self::DS, $_path);
                $dirname = array_pop($exPath);
                $skipper = (substr($dirname, 0, 1) === '.');
            }

            if (!$skipper && (empty($dirs_filter) || !in_array($_path, $dirs_filter))) {

                $dirs = self::lsDirs($path);

                if ($dirs === false) {
                    //opendir(/var/www/html/...): failed to open dir: Permission denied
                    //console::log('..opendir failed!');
                } else {

                    $files = self::lsFiles($path, $files_preg);

                    $this->_dirs []= $path;
                    $this->_files = array_merge($this->_files, $files);

                    $this->buildTree($dirs, $dirs_filter, $files_preg);

                }

            } else {
                console::log("...skipped %s", $_path);
            }
        }




    }

    /**
     * unique file name
     */
    public static function fileId($path) {
        return md5($path);
    }

    /**
     * Checksum
     */
    public static function crcFile($path) {
        return sprintf("%u", crc32(file_get_contents($path)));
    }
}

