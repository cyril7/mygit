<?php
        require_once('../Smarty/libs/Smarty.class.php');

        $smarty = new Smarty();
	$smarty -> left_delimiter="<{";
	$smarty -> right_delimiter="}>";
	$smarty -> template_dir = "./templates/";
	$smarty -> compile_dir = "./templates_c/";
        //$smarty -> assign('aa',"hello");
        //$smarty -> display("./templates/TestController2.tpl");

	$arr1=array('beijing','shanghai','tianjing');
        $smarty -> assign('arr1',$arr1);


	$arr2=array('city1'=>'beijing','city2'=>'shanghai','city3'=>'tianjing');
        $smarty -> assign('arr2',$arr2);

	$arr3=array(array('beijing','shanghai','tianjing'),array('cate','janes','jude'));
        $smarty -> assign('arr3',$arr3);

	$arr4=array(array('id'=>'001','email'=>'abc@a.com','age'=>'50'),array('id'=>'002','email'=>'b@c.com','age'=>'32'));
        $smarty -> assign('arr4',$arr4);
        $smarty -> display("TestController2.tpl");
?>
