<?php
/*
	echo "<pre>";
	var_dump($_FILES);
	echo "</pre>";

*/


	//1.获取上传文件信息
	$upfile = $_FILES['pic'];
	$typelist = array("image/jpeg","image/jpg","image/png","image/gif"); //定义允许的文件类型
	$after_upload_path = "./uploads/";
	
	//2.过滤上传文件的错误号
	if ( $upfile['error'] > 0 ) {
		//获取错误信息
		switch ($upfile['error']) {
			case 1:
				$info = "上传的文件超过了php.ini中 upload_max_filesize 选项限制的值。";
			break;
			case 2:
				$info = "上传的文件超过了HTML表单中 MAX_FILE_SIZE 选项限制的值。";
			break;
			case 3:
				$info = "上传的文件只有部分上传成功。";
			break;
			case 4:
				$info = "没有文件被上传。";
			break;
			case 6:
				$info = "找不到临时目录。";
			break;
			case 7:
				$info = "文件写入失败。";
			break;
		}
		die("上传文件错误，原因：".$info);
	}
		//3.本次上传文件到小的约束
	//if($upfile["size"] > 100000) {
	//	die("上传文件超出程序限制。");
	//}
	
	//4.类型过滤
	if( !in_array($upfile["type"],$typelist)) {
		die("上传文件类型非法。".$upfile["type"]);
	}
	
	//5.上传后的文件名(随机生成唯一文件名后缀)
	$fileinfo = pathinfo($upfile["name"]);
	do{
		$newfile = date("YmdHis").rand(1000,9999).".".$fileinfo["extension"];
	}while(file_exists($after_upload_path.$newfile));
	
	//6.执行文件上传信息
	if(is_uploaded_file($upfile["tmp_name"])){
		//执行文件上传(移动上传文件)
		if (move_uploaded_file($upfile["tmp_name"],$after_upload_path.$newfile)) {
			echo "文件上传成功！";
			echo "<h3><a href='index.php'>浏览</a></h3>";
		}
		else{
			die("上传文件失败!");
		}
	}
	else {
		die("不是一个上传文件");
	}
?>
