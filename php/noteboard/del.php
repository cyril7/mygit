<html>
	<head>
	
	</head>
	
	<body>
		<center>
			<h2>我的留言板</h2>
			<a href="index.html">添加留言</a>
			<a href="show.php">查看留言</a>
			<hr width="90%" />
			
			<h3>删除留言</h3>
				<?php
					//执行删除指定id的留言信息
					//1.获取要删除留言的id号
					$id=$_GET["id"];
					
					//2.从留言records.txt中获取留言信息
					$info = file_get_contents("/tmp/records.txt");
					
					//3.每条留言的分隔符为"@@@"
					$record_list = explode("@@@",$info);
					
					//4.使用unset删除指定id的留言
					unset($record_list[$id]);
					
					//5.写回磁盘文件
					$new_info = implode("@@@",record_list);
					file_put_contents("/tmp/records.txt",$new_info);
					
					//6.页面提示删除成功
					echo "删除成功！谢谢！";
				?>

		</center>
	</body>

</html>

