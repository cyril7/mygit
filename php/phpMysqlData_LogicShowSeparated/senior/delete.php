<?php
require_once 'smarty2_head.php';
//mysql_connect
$conn = mysql_connect(DB_HOST, DB_USER, DB_PASS) or die("connect failed" . mysql_error());
mysql_select_db(DB_DATABASENAME, $conn); 
//params
$id       = $_POST['id'];
//delete row in db
$sql = sprintf("delete from %s where id=%d", DB_TABLENAME, $id);
$result = mysql_query($sql, $conn);
mysql_close($conn);
if ($result)
  echo "t";
else
  echo "f";
?>
