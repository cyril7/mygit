<?php
        require_once('../Smarty/libs/Smarty.class.php');

        $smarty = new Smarty();
        $smarty -> left_delimiter="<{";
        $smarty -> right_delimiter="}>";
        $smarty -> template_dir = "./templates/";
        $smarty -> compile_dir = "./templates_c/";

	//define a function
	//tpl call : <{test_func times="4" size="5" color="red" content="feng"}>
	function test1($args) {
		$str = "";

		for ($i=0;$i<$args['times'];$i++) {
			$str .= "<font color='".$args['color']."' size='".$args['size']."' >".$args['content']."</font>";
		}
		return $str;
	}
	//register it
	$smarty -> registerPlugin("function","test_func","test1");
	
	//use type of 'block' for function call
	//tpl call : <test_func_block  times="4" size="5" color="red" con="feng"}></test_func_block>
	function test2($args,$con){
		if (isset ($con)) {
			$str = "";
			for ($i=0;$i<$args['times'];$i++) {
				$str .= "<font color='".$args['color']."' size='".$args['size']."' >".$con."</font>";
			}
		return $str;
		}
	}
	$smarty -> registerPlugin("block","test_func_block","test2");

	//
	function test3($args) {
		$result = '';
		switch ($args['operator']) {
			case '+':
				$result = $args['num1'] + $args['num2'];
			break;
			case '-':
				$result = $args['num1'] - $args['num2'];
			break;
			case '*':
				$result = $args['num1'] * $args['num2'];
			break;
			case '/':
				$result = $args['num1'] / $args['num2'];
			break;
		}
		return $result;
	}
	$smarty -> registerPlugin("function","test_func_math","test3");
        //$smarty -> assign('arr1',$arr1);
        $smarty -> display("TestController_func.tpl");
?>
