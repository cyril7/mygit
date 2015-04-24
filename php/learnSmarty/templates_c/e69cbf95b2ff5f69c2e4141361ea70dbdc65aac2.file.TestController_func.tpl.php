<?php /* Smarty version Smarty-3.1.11, created on 2012-08-18 01:08:29
         compiled from "./templates/TestController_func.tpl" */ ?>
<?php /*%%SmartyHeaderCode:1196080699502e6ffb3c5223-94733493%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'e69cbf95b2ff5f69c2e4141361ea70dbdc65aac2' => 
    array (
      0 => './templates/TestController_func.tpl',
      1 => 1345223186,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '1196080699502e6ffb3c5223-94733493',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.11',
  'unifunc' => 'content_502e6ffb522c30_13480318',
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_502e6ffb522c30_13480318')) {function content_502e6ffb522c30_13480318($_smarty_tpl) {?><h1>self define function</h1>
<?php echo test1(array('times'=>"6",'content'=>"hello,zhongshan",'color'=>"red",'size'=>"5"),$_smarty_tpl);?>

<h2>self define function for block call</h2>
<?php $_smarty_tpl->smarty->_tag_stack[] = array('test_func_block', array('times'=>"4",'size'=>"5",'color'=>"blue")); $_block_repeat=true; echo test2(array('times'=>"4",'size'=>"5",'color'=>"blue"), null, $_smarty_tpl, $_block_repeat);while ($_block_repeat) { ob_start();?>

ookk PRE
<?php $_block_content = ob_get_clean(); $_block_repeat=false; echo test2(array('times'=>"4",'size'=>"5",'color'=>"blue"), $_block_content, $_smarty_tpl, $_block_repeat); } array_pop($_smarty_tpl->smarty->_tag_stack);?>

<h1>self define function for doing math</h1>
<?php echo test3(array('num1'=>'3','num2'=>'10','operator'=>"+"),$_smarty_tpl);?>

<?php }} ?>