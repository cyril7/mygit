<?php
        require_once('../Smarty/libs/Smarty.class.php');

        $smarty = new Smarty();
        $smarty -> left_delimiter="<{";
        $smarty -> right_delimiter="}>";
        $smarty -> template_dir = "./templates/";
        $smarty -> compile_dir = "./templates_c/";
        //$smarty -> debugging = true ;
	$smarty -> cache_dir = '/tmp/';
        $smarty -> caching = true ;
        $smarty -> cache_lifetime = 20;

	$id =@$_GET['id'];
	//insert function
	function insert_getVisitTime() {
		$time = '';
		if ( !is_file("mycount.txt") ) {
			$time = '1';
			file_put_contents("mycount.txt",'1');
		}
		else {
			$time = file_get_contents("mycount.txt");
			$time = intval($time) + 1;
			file_put_contents('mycount.txt',$time);
		}

		return $time;
	}
	

	class Dog {
		var $name;
		public function sayHello(){
			//echo 'hellodog!';
			return 'hellodog!';
		}
	}
	$dog1 = new Dog();
	$dog1->name = 'dognamedcate';
	
	$smarty->assign('vv',$dog1);
	$smarty -> display('myindexUI.tpl',$id);
?>
