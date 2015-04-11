<?php
//万年历的实现
//1.获取当前时期信息 年月日 （默认为当前日期）
@$year = $_GET['y'] ? $_GET['y'] : date("Y"); //@号抑制"Undefied Index的Notice输出"
@$mon = $_GET['m'] ? $_GET['m'] : date("m");

//2.计算出当前月有多少天和本月1号是星期几
$day = date("t",mktime(0,0,0,$mon,1,$year)); //获取对应月的天数
$w = date("w",mktime(0,0,0,$mon,1,$year));	//获取当前月中1号是星期几


//3.输出日期的头部信息（标题和表头）
echo "<center>";
echo "<h1>{$year}年{$mon}月</h1>";
echo "<table width='600' border='1'>";
echo "<tr>";

echo "<th style='color:red'>星期日</th>";
echo "<th>星期一</th>";
echo "<th>星期二</th>";
echo "<th>星期三</th>";
echo "<th>星期四</th>";
echo "<th>星期五</th>";
echo "<th style='color:green'>星期六</th>";

echo "</tr>";


//4.循环遍历输出日期信息
$dd=1;							//代表日期是1号，每个月的第一天
while ($dd<=$day){
	echo "<tr>";
	for ( $i=0;$i<7;$i++){
		// $dd <= $day :排除 后面的空格，避免大于当月天数也显示
		// $w <= $i || $dd != 1 ：排除前面的空格，前一个月的日期在本月显示
		if ($dd <= $day && ( $w <= $i || $dd != 1 )) {
			echo "<td>{$dd}</td>";
			$dd++;
		}
		else {
			echo "<td>&nbsp</td>";
		}
	}
	echo "</tr>";
}

echo "</table>";
//5.输出上一月和下一月的超级链接
$pre_y = $next_y = $year; //年
$pre_m = $next_m = $mon; //月
if ( $mon == 1) {
	$pre_m = 12; 
	$pre_y -- ; 
}
else {
	$pre_m --;
}
if ( $mon == 12 ) {
	$next_m = 1;
	$next_y ++;
}
else {
	$next_m ++;
}

echo "<h3><a href='calender.php?y={$pre_y}&m=$pre_m'>上一月</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
echo "<a href='calender.php?y={$next_y}&m=$next_m'>下一月</a></h3>";

echo "</center>";
?>
