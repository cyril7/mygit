<?php
	//此案例演示对XML文件的更新
	//把第一个学生的年龄增加十岁 + 10
	
	//创建DOMDocument
	$xmldoc = new DOMDocument();
	
	//加载xml文件
	$xmldoc->load("newMyClass.xml");
	
	//找到这个学生
	$stus = $xmldoc->getElementsByTagName("学生");
	$stu1 = $stus->item(0);
	$stu1_age = $stu1->getElementsByTagName("年龄")->item(0);
	//最好限定这个值为整型
	$stu1_age->nodeValue += 10;
	
	$xmldoc->save("newMyClass.xml");
?>
