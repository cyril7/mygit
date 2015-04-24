<?php /* Smarty version Smarty-3.1.11, created on 2012-08-19 14:55:25
         compiled from "./templates/myindexUI.tpl" */ ?>
<?php /*%%SmartyHeaderCode:162225012850308563ea6361-28314564%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '64198ceaa90b1e0daa7b97f3800fd330b0ec1c48' => 
    array (
      0 => './templates/myindexUI.tpl',
      1 => 1345359296,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '162225012850308563ea6361-28314564',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.11',
  'unifunc' => 'content_50308564202655_61916301',
  'variables' => 
  array (
    'vv' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_50308564202655_61916301')) {function content_50308564202655_61916301($_smarty_tpl) {?><h1>Total of the visitors</h1>
<?php echo Smarty_Internal_Nocache_Insert::compile ('insert_getVisitTime',array(), $_smarty_tpl, 'null');?>

<h2>User List</h2>





<h1>get value of a OBJECT</h1>
<?php echo $_smarty_tpl->tpl_vars['vv']->value->name;?>

<?php echo $_smarty_tpl->tpl_vars['vv']->value->sayHello();?>

<?php }} ?>