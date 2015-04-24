<?php
//执行文件的修改操作

//读取配置文件
echo "<pre>";
var_dump($_POST);
echo "</pre>";

$info = file_get_contents("dbconfig.php");
//对POST进行遍历，并对配置文件进行正则替换
foreach ( $_POST as $k => $v ) {
	$info = preg_replace("/define\(\"{$k}\",\"(.*)?\"\)/","define(\"{$k}\",\"{$v}\")",$info);
}
//将替换后的信息写回到配置文件中
file_put_contents("dbconfig.php",$info);

echo "<h2>修改成功！</h2>";
echo "<a href='edit.php'>返回</a>";
?>
