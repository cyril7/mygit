<?php
//定义中英文转化
$keyinfo = array("HOST"=>"主机名","USER"=>"用户","PASS"=>"密码","DBNAME"=>"数据库","PAGESIZE"=>"页大小");
//解析配置内容到$match变量中
$info = file_get_contents("dbconfig.php");
preg_match_all("/define\(\"(.*?)\",\"(.*)?\"\)/",$info,$match);


echo "<pre>";
var_dump($match);
echo "</pre>";


//
echo "<h2>编辑配置文件</h2>";
echo "<form action='doupdate.php' method='post'>";

foreach ($match[1] as $k=>$v) {
	echo "{$keyinfo[$v]}:<input type='text' name='{$v}' value='{$match[2][$k]}'><br/><br/>";
}
echo "<input type='submit' value='编辑'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
echo "<input type='submit' value='重置'>";
echo "</form>";
?>
