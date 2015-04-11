<?php
header("Content-Type: text/html; charset=utf-8");
//require('../../smart_libs/Smarty.class.php');
require('../Smarty/libs/Smarty.class.php');
require_once('smarty2_head.php');
date_default_timezone_set("PRC");

//mysql_connect
$conn = mysql_connect(DB_HOST, DB_USER, DB_PASS) or die("connect failed" . mysql_error());
mysql_select_db(DB_DATABASENAME, $conn);

//个数
$sql = sprintf("select count(*) from %s", DB_TABLENAME);
$result = mysql_query($sql, $conn);
if ($result)
{
	$dbcount = mysql_fetch_row($result);
	$tpl_db_count = $dbcount[0];
}
else
{
	die("query failed");
}
$tpl_db_tablename = DB_TABLENAME;
$tpl_db_coltitle = $dbcolarray;
//表中内容
$tpl_db_rows = array();
$sql = sprintf("select %s from %s", implode(",",$dbcolarray), DB_TABLENAME);
$result = mysql_query($sql, $conn);
while ($row = mysql_fetch_array($result, MYSQL_ASSOC))//等价$row=mysql_fetch_assoc($result)
	$tpl_db_rows[] = $row;

mysql_free_result($result);
mysql_close($conn);

$tpl = new Smarty;
$tpl->assign('db_tablename', $tpl_db_tablename);
$tpl->assign('db_count', $tpl_db_count);
$tpl->assign('db_coltitle', $tpl_db_coltitle);
$tpl->assign('db_rows', $tpl_db_rows);

$tpl->display('smarty2.html');
?>
