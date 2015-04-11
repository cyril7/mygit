<?php
require_once 'smarty2_head.php';
//mysql_connect
$conn = mysql_connect(DB_HOST, DB_USER, DB_PASS) or die("connect failed" . mysql_error());
mysql_select_db(DB_DATABASENAME, $conn);
//params
$name = $_POST['name'];
$age = $_POST['age'];
//insert db
$sql = sprintf("INSERT INTO %s(name, age) VALUES('%s', %d)", DB_TABLENAME, $name, $age);
$result=mysql_query($sql, $conn);
if ($result)
  echo mysql_insert_id($conn);
else
  echo "f";
mysql_close($conn);
?>
