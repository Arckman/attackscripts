<?php

//包含配置文件中的参数
$config = include_once 'myconf.php';//包含配置文件
if (isset($config['wlog_dir'])) {
    $log_path = $config['wlog_dir'];
    //---当且仅当配置了log_path才进行日志记录
    $http_request = new http_request();
		$resp = $http_request->raw();
		$cap = nl2br($resp)."<br><hr>";
		#echo $log_path.$http_request->remoteAddr().".html";
		if(!file_exists($log_path.$http_request->remoteAddr().".html")){
				mkdirs($log_path);//如果目录不存在则创建
		    $aaa=file_put_contents($log_path.$http_request->remoteAddr().".html",$cap);
		    #var_dump($aaa);
		}else{
				#mkdirs($$log_path);//如果目录不存在则创建
		    $aaa=file_put_contents($log_path.$http_request->remoteAddr().".html",$cap,FILE_APPEND);
		    #var_dump($aaa);
		}
}
if (isset($config['attacklog_dir'])) {
    		$attacklog_dir = $config['attacklog_dir'];
    		$Catchs = new MagicBlue($attacklog_dir);
    		$Catchs->Flow();
    		//it shouldn't be turned on unless everyone is using their waf...
   		$Catchs->waf($turn_on=true);
		#echo "fasdf";
    }
?>
<?php
//流量监控定义
class http_request {
    public $add_headers = array('CONTENT_TYPE', 'CONTENT_LENGTH');

    function http_request($add_headers = false) {

        $this->retrieve_headers($add_headers);
        $this->body = @file_get_contents('php://input');
    }

    function retrieve_headers($add_headers = false) {

        if ($add_headers) {
            $this->add_headers = array_merge($this->add_headers, $add_headers);
        }

        if(isset($_SERVER['REMOTE_ADDR'])){
            $this->remoteAddr=$_SERVER['REMOTE_ADDR'];
        }else{
            $this->remoteAddr='unknown';
        }

        if (isset($_SERVER['HTTP_METHOD'])) {
            $this->method = $_SERVER['HTTP_METHOD'];
            unset($_SERVER['HTTP_METHOD']);
        } else {
            $this->method = isset($_SERVER['REQUEST_METHOD']) ? $_SERVER['REQUEST_METHOD'] : false;
        }
        $this->protocol = isset($_SERVER['SERVER_PROTOCOL']) ? $_SERVER['SERVER_PROTOCOL'] : false;
        $this->request_method = isset($_SERVER['REQUEST_METHOD']) ? $_SERVER['REQUEST_METHOD'] : false;

        $this->headers = array();
        foreach($_SERVER as $i=>$val) {
            if (strpos($i, 'HTTP_') === 0 || in_array($i, $this->add_headers)) {
                $name = str_replace(array('HTTP_', '_'), array('', '-'), $i);
                $this->headers[$name] = $val;
            }
        }
    }

    /** 
    * Retrieve HTTP Method
    */
    function method() {
        return $this->method;
    }

    /** 
    * Retrieve HTTP Body
    */
    function body() {
        return $this->body;
    }

    /**
     * Retrieve remote addr
     */
    function remoteAddr() {
        return $this->remoteAddr;
    }

    /** 
    * Retrieve an HTTP Header
    * @param string Case-Insensitive HTTP Header Name (eg: "User-Agent")
    */
    function header($name) {
        $name = strtoupper($name);
        return isset($this->headers[$name]) ? $this->headers[$name] : false;
    }

    /**
    * Retrieve all HTTP Headers 
    * @return array HTTP Headers
    */
    function headers() {
        return $this->headers;
    }

    /**
    * Return Raw HTTP Request (note: This is incomplete)
    * @param bool ReBuild the Raw HTTP Request
	* 这里可以设置过滤规则
    */
    function raw($refresh = false) {
        if (isset($this->raw) && !$refresh) {
            return $this->raw; // return cached
        }
        $headers = $this->headers();
        $this->raw = "{$this->method} {$_SERVER['REQUEST_URI']} {$this->protocol}\r\n";

        foreach($headers as $i=>$header) {
                $this->raw .= "$i: $header\r\n";
        }
        $this->raw .= "\r\n{$this->body}";

        return $this->raw;
    }

}

function mkdirs($dir, $mode = 0777)
{
   			if (is_dir($dir) || @mkdir($dir, $mode)) return TRUE;
   		 	if (!mkdirs(dirname($dir), $mode)) return FALSE;
   		 	return @mkdir($dir, $mode);
} 
?>


<?php
//WAF类定义
    
    class MagicBlue
    {
        public function __construct($filepath)
        {
            $this->filepath = $filepath;
            $this->header = array();
            $this->files = array();
        }

        public function Flow()
        {
            $arr = array('HTTP_HOST','HTTP_USER_AGENT','HTTP_ACCEPT','HTTP_ACCEPT_LANGUAGE','HTTP_ACCEPT_ENCODING','HTTP_REFERER','HTTP_COOKIE','HTTP_X_FORWARDED_FOR','HTTP_CONNECTION');
            $HTTP_Method = $_SERVER['REQUEST_METHOD'];
            $server = $_SERVER;
            if(!file_exists($this->filepath))
            {
                mkdir($this->filepath,0777);
            }
            $filename = date('Y-m-d-h');
            $Allfilepath = $this->filepath.'/'.$filename.".html";
            foreach($arr as $value)
            {
            		if(isset($server[$value]))
            		{
                		$this->header[$value] = $server[$value];
                }
            }
            $head = '';
            foreach ($this->header as $key => $value)
            {
                if(stripos($key, 'HTTP_') == -1)
                {
                    $key = ucwords(strtolower($key));
                }else
                {
                    $key = ucwords(strtolower(substr($key, 5)));
                }
                $head.= $key.': '.$value."<br />";
            }
            $request_url = $_SERVER['REQUEST_URI'];
            $protocol = $_SERVER['SERVER_PROTOCOL'];
            if(isset($_POST))
            {
                $post = file_get_contents('php://input');
            }
            $ip = $_SERVER['REMOTE_ADDR'];
            $time = date('Y/m/d h:i:s');

            $file = $_FILES;
            if(isset($file)){
                foreach ($file as $key => $value){
                    $this->files['content'] = file_get_contents($value['tmp_name']);
                }
            }
            //$content = $ip."\t".$time."\t\n".$HTTP_Method.' '.$request_url.' '.$protocol."\r\n".$head."\n\n".$post."\n\n".(isset($this->files['content'])?($this->files['content']."\n\n"):"");
            $content = $ip."\t".$time."<br />".$HTTP_Method.' '.$request_url.' '.$protocol."<br />".$head."<br /><br />".$post."<br /><br />".(isset($this->files['content'])?($this->files['content']."\n\n"):"")."<hr>";
            $this->WriteFile($Allfilepath,$content,FILE_APPEND);
        }

        public function WriteFile($filepath,$content,$FILE_APPEND=FILE_APPEND)
        {
            file_put_contents($filepath,$content,$FILE_APPEND);
        }


        public function waf($turn_on=true){
            if($turn_on){
                $get = $_GET;
                $post = $_POST;
                $cookie = $_COOKIE;
                $files = $this->files;
                $server = $_SERVER;
                $input = array("Get"=>$get,"Post"=>$post,"Cookie"=>$cookie,"Server"=>$server,"upload"=>$files);
            		$pattern = "select|insert|update|delete|and|union|load_file|outfile|dumpfile|sub|hex";
            		$pattern .= "|file_put_contents|fwrite|system|eval|assert|file:\/\/";
            		$pattern .="|passthru|exec|system|chroot|scandir|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore";
           		  $pattern .="|`|dl|openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|assert|pcntl_exec";
                $vpattern = explode("|",$pattern);
            		$bool = false;
		            foreach ($input as $k => $v) {
		                foreach($vpattern as $value){
		                    foreach ($v as $kk=> $vv) {
		                        if (preg_match( "/$value/i", $kk )||preg_match("/$value/i", $vv)){
		                            $bool = true;
		                            /////  => fuck  Location  最好的那个队伍
		                            #var_dump($value);
		                            die();
		                            break;
		                        }
		                    }
		                    if($bool) break;
		                }
		                if($bool) break;
		            }
            }
        }
    }
?>

