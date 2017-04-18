<?php
$_SERVER["PHP_SELF"] ;
if(isset($_POST['server']) and isset($_POST['ip'])){
	$server=$_POST['server'];
	$ip=$_POST['ip'];
	$selfkill=$_POST['selfkill']?true:false;
    $port=55168;

    $message='HelloWorld!';
    $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or die("Could not create socket\n");
    socket_sendto($socket, $message, strlen($message),0,$server,$port) or die("Could not send data to server\n");
	
}
?>
<form	action="client.php" method="post">
	Server IP:<input type="text" name="server">
    flag IP:<input type="text" name="ip">
    SelfKill:<input type="checkbox" name="selfkill">
    <input type="submit" value="GO!!!">
</form>