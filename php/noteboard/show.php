<html>
	<head>
	
	</head>
	
	<body>
		<center>
			<h2>我的留言板</h2>
			<a href="index.html">添加留言</a>
			<a href="show.php">查看留言</a>
			<hr width="90%" />
			
			<h3>查看留言</h3>
			<table border="1" width="700">
				<tr>
					<th>留言标题</th>
					<th>留言人</th>
					<th>留言内容</th>
					<th>IP地址</th>
					<th>留言时间</th>
					<th>操作</th>
				</tr>
				
				<?php
					//获取留言信息，解析后输出到表格中
					
					//1.从留言records.txt中获取留言信息
					$info = file_get_contents("/tmp/records.txt");
					
					//2.取出每条留言最后的"@@@"符号
					$info = rtrim($info,"@");
					
					//3.每条留言的分隔符为"@@@"
					$record_list = explode("@@@",$info);
					
					//4.遍历每条信息数组，对每条留言做再次解析
					//	此时分隔符为"##"
					foreach ( $record_list as $key=>$value ) {
						$record = explode("##",$value);
						echo "<tr>";
						echo "<td>$record[0]</td>";
						echo "<td>$record[1]</td>";
						echo "<td>$record[2]</td>";
						echo "<td>$record[3]</td>";
						echo "<td>".date("Y-m-d H:i:s",$record[4])."</td>";
						echo "<td><a href='del.php?id={$key}'>删除</a></td>";
						echo "</tr>";
					}
				?>

		</center>
	</body>

</html>
