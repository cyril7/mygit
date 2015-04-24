<?php
	//此案例演示对XML文件的增删改
	
	//创建DOMDocument
	$xmldoc = new DOMDocument();
	
	//加载xml文件
	$xmldoc->load("newMyClass.xml");
	
	//删除一个学生信息
	//取出根节点
	$root = $xmldoc->getElementsByTagName("班级")->item(0);
	
	//删除第三个学生
	//找到该学生
	$stus = $xmldoc->getElementsByTagName("学生");
	$stu1 = $stus->item(2);
	//可以从根节点的子节点列表中删除找到的子节点
	//$root->removeChild($stu1);
	//也可以从找到的子节点的父节点直接删除自己
	$stu1->parentNode->removeChild($stu1);
	
	$xmldoc->save("newMyClass.xml");
?>
