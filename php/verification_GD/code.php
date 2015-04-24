<?php

//绘制验证码
//字体文件位置
$font = "/usr/share/fonts/chinese/TrueType/uming.ttf";
//验证码的长度
$num = 4;
$type = 0;
//获取需要的验证码值
$str = getCode($num,$type);

//创建一个画布，分配颜色
$width = $num * 20;							//宽度
$height = 30;								//高度
$im = imagecreatetruecolor($width,$height); //设定画布宽高

//定义几个颜色，输出不同颜色的验证码
$color[] = imagecolorallocate($im,111,0,55);		//字体颜色
$color[] = imagecolorallocate($im,0,77,0);		//字体颜色
$color[] = imagecolorallocate($im,0,0,160);		//字体颜色
$color[] = imagecolorallocate($im,221,111,0);		//字体颜色
$color[] = imagecolorallocate($im,220,0,0);		//字体颜色
$bg = imagecolorallocate($im,240,240,240);	//背景颜色
	
//开始绘画
imagefill($im,0,0,$bg);
imagerectangle($im,0,0,$width-1,$height-1,$color[rand(0,4)]); //设定边框
//绘制干扰点
for ( $i=0;$i<200;$i++) {
	$c = imagecolorallocate($im,rand(0,255),rand(0,255),rand(0,255)); //随机 红绿蓝 三色
	imagesetpixel($im,rand(0,$width),rand(0,$height),$c);
}

//绘制五条干扰线
for ( $i=0;$i<5;$i++) {
	$c = imagecolorallocate($im,rand(0,255),rand(0,255),rand(0,255)); //随机 红绿蓝 三色
	imageline($im,rand(0,$width),rand(0,$height),rand(0,$width),rand(0,$height),$c);
}

//绘制验证码 需要逐个字母输出
for ($i=0;$i<$num;$i++) {
	imagettftext($im,18,rand(-40,40),8+(18*$i),24,$color[rand(0,4)],$font,$str[$i]);				//图像源，字体大小，倾斜角度，位置，高度,颜色
}

//输出图像
header("Content-Type:image/png");			//设定响应头
imagepng($im);

//销毁图片 释放内容
imagedestroy($im);

/**
  * 随机生成一个验证码的内容
  * @param $m 验证码的个数 默认为4
  * @param $type 验证码的类型: 0:纯数字 1：数字+小写字母 2:数字+大小写字符
**/	

function getCode($m=4,$type=0) {
	//62个字符的字符串总集
	$str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	//echo strlen($str);
	//0到9是数字，10到35是小写字母，36到61是大写字母
	$t = array(9,35,strlen($str)-1);
	
	//随机生成验证码所需内容
	$c = "";
	for($i=0;$i<$m;$i++) {
		$c .= $str[rand(0,$t[$type])];
	}
	//echo $c;
	return $c;
}

//getCode();
?>
