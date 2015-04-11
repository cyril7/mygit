<?php
//简单的文件管理（指定目录）

$path = "./";
$self_name_file = basename(__FILE__); //本脚本文件名，不含目录名
$file_exclue = array($self_name_file);

//根据action的信息值，做对应操作
switch ( @$_GET['action']) {
	case "del":		//删除一个文件
	unlink($_GET["filename"]);
	break;
	
	case "create":	//创建一个文件
	$filename=trim($path,"/")."/".$_POST["filename"];
	if (file_exists($filename)) {
		die ("要创建的文件已经存在！");
	}
	//创建这个文件
	$f = fopen($filename,"w");
	fclose($f);
	break;
	
	case "edit":	//查看原有文件内容并提供表单进行修改
	$filename = $_GET["filename"];
	$fileinfo = file_get_contents($filename);
	break;
	
	case "update";	//提交修改后的表单内容
	//获取信息：文件名 内容
	$filename = $_POST["filename"];
	$content = $_POST["content"];
	//执行文件内容修改
	file_put_contents($filename,$content);
	break;
}

//浏览指定目录下的文件

if ( !file_exists($path) && !is_dir($path) ) {
	die($path."目录无效！");
}

//输出表头信息
echo "<h3>{$path}目录下的文件信息</h3>";
echo "<h4><a href='{$self_name_file}?action=add'>创建文件</a></h4>";
echo "<table width='600' border='1'>";
echo "<tr bgcolor='#cccccc' align='left'>";
	echo "<th>序号</th><th>名称</th><th>类型</th><th>大小</th><th>创建时间</th><th>操作</th>";
echo "</tr>";


//打开目录，并遍历目录下的文件
$dir = opendir($path);
if($dir) {
	$i=0;
	while($f = readdir($dir)) {
		if ( $f == "." || $f == ".." || in_array($f,$file_exclue)) {
			continue;
		}
		$file = trim($path,"/")."/".$f;
		$i++;
		echo "<tr>";
		echo "<td>{$i}</td>";
		echo "<td>{$f}</td>";
		echo "<td>".filetype($file)."</td>";
		echo "<td>".filesize($file)."</td>";
		echo "<td>".date("Y-m-d H:i:s",filectime($file))."</td>";
		echo "<td><a href='{$self_name_file}?filename={$file}&action=del'>删除</td>";
		echo "<td><a href='{$self_name_file}?filename={$file}&action=edit'>编辑</td>";
		echo "</tr>";
	}
	closedir($dir);
}
echo "<tr bgcolor='#cccccc' align='left'><td colspan='6'>&nbsp;</td><tr>";
echo "</table>";

//case "add" 操作，新建文件需要创建表单
if ( @$_GET['action'] == "add") {
	echo "<form action='{$self_name_file}?action=create' method='post'>";
	echo "新建文件: <input type='text' name='filename' size='12'/>";
	echo "<input type='submit' value='新建文件' />";
	echo "</form>";
}

//case "edit" 操作，编辑文件需要创建表单
if ( @$_GET['action'] == "edit") {
	echo "<br/><br/><br/><br/><form action='{$self_name_file}?action=update' method='post'>";
	echo "<input type='hidden' name='filename' value='{$filename}' /> ";
	echo "文件名: {$filename}<br/><br/>";
	echo "文件内容: <textarea name='content' cols='40' rows='6'>{$fileinfo}</textarea><br/>";
	echo "<input type='submit' value='编辑完毕' />";
	echo "</form>";
}
?>	
