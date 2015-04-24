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
			<?php include("menu.php") ;//导入导航栏；?> 
			
			<h3>分页浏览新闻</h3>
			
			<!-------搜索表单--------->
			<form action="list3.php" method="get">
				标题：<input type="text" name="title" size="8" value="<?php echo @$_GET['title'];?>"/>&nbsp;&nbsp;&nbsp;
				关键字：<input type="text" name="keywords" size="8" value="<?php echo @$_GET['keywords'];?>"/>&nbsp;&nbsp;&nbsp;
				作者：<input type="text" name="author" size="8" value="<?php echo @$_GET['author'];?>"/>&nbsp;&nbsp;&nbsp;
				<input type="submit" value="搜索" />
				<input type="button" value="全部新闻" onclick="window.location='list3.php'" />
			</form>
			<!---------------->
			<table width="800" border="1">
				<tr>
					<th>新闻id</th><th>新闻标题</th><th>关键字</th>
					<th>作者</th><th>发布时间</th><th>新闻内容</th>
					<th>操作</th>
				</tr>
				<?php
					//封装搜索信息
					//定义一个封装搜索条件的数组变量
					$wherelist = array();
					
					//用于放置到URL参数的数组变量
					$urllist = array();
					
					//判断某个搜索栏是否有值，封装相应sql
					if (!empty($_GET["title"])) {
						$wherelist[] = "title like '%{$_GET['title']}%'";
						$urllist[] = "title={$_GET['title']}";
					}
					if (!empty($_GET["keywords"])) {
						$wherelist[] = "keywords like '%{$_GET['keywords']}%'";
						$urllist[] = "keywords={$_GET['keywords']}";
					}
					if (!empty($_GET["author"])) {
						$wherelist[] = "author like '%{$_GET['author']}%'";
						$urllist[] = "author={$_GET['author']}";
					}
					
					//组装搜索条件
					if ( count($wherelist) > 0) {
						$where = " where ".implode(" and ",$wherelist);
						$url = "&".implode("&",$urllist);
					}
					else {
						$where = " ";
						$url = " ";
						
					}
					//1.导入配置文件
					require("dbconfig.php");
					
					//2.连接mysql，选择DB
					$link = mysql_connect(HOST,USER,PASS) or die("DB connect fail!");
					mysql_select_db(DBNAME,$link); 
					
					//2.1 分页处理代码
					//=======================
						//1.定义一些分页变量
						$page=isset($_GET['page']) ? $_GET['page'] : 1;				//当前页号
						$pageSize=3;			//页大小，3条数据一页
						$maxRows;			//最大数据条
						$maxPages;				//最大页数
						
						//2.获取最大数据条数
						$sql = "select count(*) from ".TBNAME."{$where}";
						$res = mysql_query($sql,$link);
						$maxRows = mysql_result($res,0,0);
						
						//3.计算出共计最大页数
						$maxPages = ceil($maxRows/$pageSize);
						//4.判断页数是否越界，效验当前页数，防止手动输入?page=5000此类行为
						if ( $page > $maxPages ) {
							$page = $maxPages;
						}
						if ($page<1) {
							$page = 1;
						}
						
						//5.拼装分页sql语句片段
						//起始位置是当前页数减一乘以页大小
						$limit = " limit ".(($page-1)*$pageSize).",{$pageSize}";
					//=======================
					
					//3.执行查询
					$sql = "select * from ".TBNAME." {$where} order by addtime desc {$limit}";
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
			
				<?php
					//输出分页信息，显示上一页和下一页的链接
					echo "<br/><br/>";
					echo "当前{$page}/{$maxPages}页 共计{$maxRows}条";
					echo "<a href='list3.php?page=1{$url}'>首页</a>";
					echo "<a href='list3.php?page=".($page-1)."{$url}'>上一页</a>";
					echo "<a href='list3.php?page=".($page+1)."{$url}'>下一页</a>";
					echo "<a href='list3.php?page={$maxPages}{$url}'>末页</a>";
				?>

		</center>
	
	</body>
</html>
