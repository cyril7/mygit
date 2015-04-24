<?php
/*
简单的PHP作为数据源model 给 intro.tpl 分配给它需要的数据

$title = "我文章的标题";
$content = "我文章的内容";


*/
// intro.php 是一个控制器 mvc --> controller
//使用smarty 去给intro.pl 分配给它需要的数据

//使用MyMiniSmatry.class.php
require_once 'MyMiniSmarty.class.php';

$mysmarty = new MyMiniSmarty;

$mysmarty->assign("title","我的第一个文件title");
$mysmarty->assign("content","<font color='red'>我的第一个文件内容</font>");
$mysmarty->display("intro.tpl");
?>
