<?php
	require ('config.inc.php'); 		//加载数据库配置文件
	$pagesize = 5; 						//设定每页显示条目数
	if(isset($_GET['page'])&&$_GET['page']!='') {
		$page=$_GET['page'];
		}else {
		$page=0;
	}
	//连表组合查询SQL语句
	$sql = "SELECT c1 . * , c2.reply_time, c2.reply FROM info c1 LEFT JOIN reply c2 ON ( c1.id = c2.info_id ) ORDER BY c1.id DESC";
	$numRecord = mysql_num_rows(mysql_query($sql)); 				//获得结果集中的记录数
	$totalpage = ceil($numRecord/$pagesize); 						//获得总页数
	$recordSql = $sql. " LIMIT ".$page*$pagesize.",".$pagesize; 	//拼接翻页SQL语句
	$result = mysql_query($recordSql);
?>
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>留言板</title>
	<link href="style.css" rel="stylesheet" type="text/css" />
	</head>
	<body>
	<!--中部内容开始-->
	<div id="content">
	<div id="main">
	<ul>
		<li id="main_top"></li>
		<li id="main_middle" style="padding: 0px 0px 15px 0px;">
		<div class="title_cr">留言板</div>
		<?php
	//循环嵌套开始
	while($rs=mysql_fetch_object($result)){
	?>
		<table width="872" border="0" align="center" cellpadding="0"
			cellspacing="0" class="tab_bbs">
			<tr>
				<td colspan="2" class="title_bbs">
				<table width="100%" border="0" cellspacing="0" cellpadding="0">
					<tr>
						<td width="50" class="title_b">&nbsp;</td>
						<td width="400" class="title_b"><a href="reply.php?id=<?php
						echo $rs->id?>">回复</a> | <a href="delete.php?id=<?php echo
						$rs->id?>">删除</a> &nbsp;&nbsp;&nbsp;&nbsp;建议</td>
						<td width="100" class="title_b"><!--留言人--> <?php echo $rs->name?>
						<!--留言人--></td>
						<td class="title_b"><!--留言时间--> <?php echo date("Y-m-d H:i:s",$rs->content_time+8*3600)?>
						<!--留言时间--></td>
					</tr>
				</table>
				</td>
			</tr>
			<tr>
				<td width="45">&nbsp;</td>
				<td width="823" class="td_bbs"><!--留言内容--> <?php echo nl2br(htmlspecialchars($rs->content))?>
				<!--留言内容--></td>
			</tr>
			<tr>
				<td width="45" class="td_bbswhite">&nbsp;</td>
				<td class="td_bbsgray">回复标题：你好 回复人：管理员 回复时间： <?php if($rs->reply_time!="") echo date("Y-m-d H:i:s",$rs->reply_time+8*3600)?></td>
			</tr>
			<tr>
				<td width="45" class="td_bbs">&nbsp;</td>
				<td><!--回复留言内容--> <?php echo nl2br(htmlspecialchars($rs->reply))?>
				<!--回复留言内容--></td>
			</tr>
		</table>
		<?php
	//循环嵌套收尾
	}
	?>
		<div style="clear: both;"></div>
		<div id="dashline"></div>
		<!--页码开始-->
		<div id="page" style="margin-right: 30px; margin-top: 8px;"><span
			class="grayborder" style="background-color: #F6F6F6;"> <a
			href='index.php?page=<?php if ($page<$totalpage-1) echo
		$page+1;?>'>下一页</a> </span> <span class="grayborder"
			style="background-color: #F6F6F6;"> <a href='index.php?page=<?php
		if ($page>0) echo $page-1;?>'>上一页</a> </span></div>
		<!--页码结束--></li>
		<li id="main_bt"></li>
	</ul>
	</div>
