<html>
	<head>
	
	</head>
	
	<body>
		<center>
			<h2>我的留言板</h2>
			<a href="index.html">添加留言</a>
			<a href="show.php">查看留言</a>
			<hr width="90%" />
			
			<h3>添加留言</h3>
			<?php
				//执行留言信息添加操作
				
				//1.获取要添加的留言信息(title,author,content)，
				//	并且补上其他辅助信息(ip地址、添加时间)
				$title = $_POST["title"];
				$author = $_POST["author"];
				$content = $_POST["content"];
				$ip = $_SERVER["REMOTE_ADDR"];
				$addtime = time();
				
				//2.拼装（组装）留言信息，以"@@@"添加到末尾作为分隔符
				$record = "{$title}##{$author}##{$content}##{$ip}##{$addtime}@@@";
				//echo $record;
				
				
				//3.将留言信息追加到records.txt中
				$info=file_get_contents("/tmp/records.txt");	//获取之前的留言信息
				file_put_contents("/tmp/records.txt",$info.$record);
				
				//4.输出留言成功
				echo "留言成功！谢谢！";
			?>
		</center>
	</body>

</html>
