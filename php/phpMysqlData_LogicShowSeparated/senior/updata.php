<?php
require_once 'smarty2_head.php';
//mysql_connect
$conn = mysql_connect(DB_HOST, DB_USER, DB_PASS) or die("connect failed" . mysql_error());
mysql_select_db(DB_DATABASENAME, $conn);  
//params
$id       = $_POST['id'];
$name = $_POST['name'];
$age = $_POST['age'];
//updata db
$sql = sprintf("update %s set name='%s',age=%d where id=%d", DB_TABLENAME, $name, $age, $id);
$result=mysql_query($sql, $conn);
mysql_close($conn);
if ($result)
  echo "t";
else
  echo "f";
?>
