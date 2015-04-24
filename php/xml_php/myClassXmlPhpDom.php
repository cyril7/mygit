<?php
	//此案例演示对XML文件的增删改
	
	//创建DOMDocument
	$xmldoc = new DOMDocument();
	
	//加载xml文件
	$xmldoc->load("myClass.xml");
	
	//添加一个学生信息
	//取出根节点
	$root = $xmldoc->getElementsByTagName("班级")->item(0);
	
	//创建学生节点
	$stu_node = $xmldoc->createElement("学生");
	
	// *********** 创建 学生节点的 属性 节点 ************ //
	$stu_node->setAttribute("性别","男");
	//创建名字节点
	$stu_node_name = $xmldoc->createElement("名字");
	$stu_node_name->nodeValue="吴君如";
	//把名字节点挂载到学生节点下
	$stu_node->appendChild($stu_node_name);
	
	//创建年龄节点
	$stu_node_age = $xmldoc->createElement("年龄");
	$stu_node_age->nodeValue="33";
	//把年龄节点挂载到学生节点下
	$stu_node->appendChild($stu_node_age);
	
	//创建介绍节点
	$stu_node_intro = $xmldoc->createElement("介绍");
	$stu_node_intro->nodeValue="美女";
	//把介绍节点挂载到学生节点下
	$stu_node->appendChild($stu_node_intro);
	
	//把学生节点挂载到根节点下即可
	$root->appendChild($stu_node);
	
	//print_r($root);
	$xmldoc->save("newMyClass.xml");
?>
