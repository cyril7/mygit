<html>
	<head>
		<title>新闻管理系统</title>
	</head>
	<body>
		<center>
			<?php 
				//导入导航栏；
				include("menu.php"); 
				//1.导入配置文件
				require("dbconfig.php");
				
				//2.连接MYSQL 并选择DB
				$link = mysql_connect(HOST,USER,PASS) or die("DB connect fail!");
				mysql_select_db(DBNAME,$link);
				
				//3.获取要修改信息的id号，并拼装查看的SQL并执行查询获取要修改的信息
				$id = $_GET['id'];
				$sql = "select * from ".TBNAME." where id = {$id}";
				$result = mysql_query($sql,$link);
				
				//4.判断是否有获取到要修改的信息
				if ( $result && mysql_num_rows($result) > 0) {
					$news = mysql_fetch_assoc($result);
				}
				else {
					die ("No information founded!");
				}
			?> 
			
			<h3>编辑新闻</h3>
			<form action="action.php?action=update" method="post">
			<input type="hidden" name="id" value="<?php echo $news['id'];?>"/>
				<table width="320" border="1">
					<tr>
						<td align="right">标题：</td>
						<td><input type="text" name="title" value="<?php echo $news['title'];?>"/></td>
					</tr>
					<tr>
						<td align="right">关键字：</td>
						<td><input type="text" name="keywords" value="<?php echo $news['keywords'];?>"/></td>
					</tr>
					<tr>
						<td align="right">作者：</td>
						<td><input type="text" name="author" value="<?php echo $news['author'];?>"/></td>
					</tr>
					<tr>
						<td align="right">内容：</td>
						<td><textarea cols="25" rows="5" name="content" /><?php echo $news['content'];?></textarea></td>
					</tr>
					<tr>
						<td colspan="2" align="center">
							<input type="submit" value="编辑" />&nbsp;&nbsp;&nbsp;&nbsp;
							<input type="reset" value="重置" />
						</td>
					</tr>
				</table>
			</form>
		</center>
	
	</body>
</html>
