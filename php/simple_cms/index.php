<html>
	<head>
		<title>新闻管理系统</title>
		<script type="text/javascript">
			function dodel(id) {
				if ( confirm("确定要删除吗？")) {
					window.location="action.php?action=del&id="+id;
				}
			}
		</script>
	</head>
	<body>
		<center>
			<?php include("menu.php") //导入导航栏；?> 
			
			<h3>浏览新闻</h3>
			<table width="800" border="1">
				<tr>
					<th>新闻id</th><th>新闻标题</th><th>关键字</th>
					<th>作者</th><th>发布时间</th><th>新闻内容</th>
					<th>操作</th>
				</tr>
				<?php
					//1.导入配置文件
					require("dbconfig.php");
					
					//2.连接mysql，选择DB
					$link = mysql_connect(HOST,USER,PASS) or die("DB connect fail!");
					mysql_select_db(DBNAME,$link); 
					
					//3.执行查询
					$sql = "select * from ".TBNAME." order by addtime desc";
					$result = mysql_query($sql,$link);
					
					//4.解析结果集，遍历输出
					while ( $row = mysql_fetch_assoc($result)) {
						echo "<tr>";
						echo "<td>{$row['id']}</td>";
						echo "<td>{$row['title']}</td>";
						echo "<td>{$row['keywords']}</td>";
						echo "<td>{$row['author']}</td>";
						echo "<td>".date("Y-m-d H-i-s",$row['addtime'])."</td>";
						echo "<td>{$row['content']}</td>";
						echo "<td>
							<a href='javascript:dodel({$row['id']})'>删除</a> 
							<a href='edit.php?id={$row['id']}'>修改</a>
							</td>";
						echo "</tr>";
					
					}
					
					//5.释放结果集
					mysql_free_result($result);
					mysql_close($link);
				?>
			</table>

		</center>
	
	</body>
</html>
