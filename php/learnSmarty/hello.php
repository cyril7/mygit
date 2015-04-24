<?php
	require_once('../Smarty/libs/Smarty.class.php');
	
	$smarty = new Smarty;
	$smarty -> assign('var1',"hello,world");
	$smarty -> display("hello.tpl");
?>
