<?php

        require_once('../Smarty/libs/Smarty.class.php');

        $smarty = new Smarty();
        $smarty -> left_delimiter="<{";
        $smarty -> right_delimiter="}>";
        $smarty -> template_dir = "./templates/";
        $smarty -> compile_dir = "./templates_c/";

function remove_dw_comments($tpl_source, &$smarty)
{
	//echo 'okok';
	//exit();
 	return preg_replace("/<!--#.*-->/U","",$tpl_source);
}
$smarty->registerFilter('pre','remove_dw_comments');

function add_header_comment($tpl_source, &$smarty)
{
 	return "<?php echo \" Created by FENGZHICHAO! \"?>".$tpl_source;
}

$smarty->registerFilter('post','add_header_comment');
function highlight($tpl_source, &$smarty)
{
 	return str_replace('smarty','<font color="red"><b>smarty</b></font>',$tpl_source);
}

$smarty->registerFilter('output','highlight');
$smarty->display("myfilter.tpl");
?>

